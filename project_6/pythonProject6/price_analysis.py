import psycopg2
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning)

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "user": "postgres",
    "password": "example",
    "database": "testdb"
}

def main():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        query = """
            SELECT 
                p.product_name,
                p.category,
                pr.price
            FROM prices pr
            JOIN products p ON pr.product_id = p.product_id
            WHERE pr.price IS NOT NULL  -- исключаем пропуски
        """
        cur.execute(query)

        cols = [desc[0] for desc in cur.description]
        df = pd.DataFrame(cur.fetchall(), columns=cols)

        if df.empty:
            print(" Данные не найдены. Проверьте связь таблиц, имена колонок или наличие записей в prices.")
            cur.close();
            conn.close();
            return

        df['price'] = df['price'].astype(float)

        cur.close()
        conn.close()

        print(f" Загружено записей: {len(df):,}\n")

        print("=== 3. Статистика по ценам ===")
        print(f"Среднее:        {df['price'].mean():,.2f} руб.")
        print(f"Медиана:        {df['price'].median():,.2f} руб.")
        print(f"Ст. отклонение: {df['price'].std():,.2f} руб.")
        print(f"Минимум:        {df['price'].min():,.2f} руб.")
        print(f"Максимум:       {df['price'].max():,.2f} руб.")

        q1, q2, q3 = df['price'].quantile([0.25, 0.5, 0.75])
        iqr = q3 - q1
        print(f"\n=== 4. Квартили ===")
        print(f"Q1: {q1:.2f} | Q2 (медиана): {q2:.2f} | Q3: {q3:.2f} | IQR: {iqr:.2f}")
        print("\n Товары с ценой выше Q3:")
        above = df[df['price'] > q3][['product_name', 'category', 'price']].drop_duplicates()
        print(above.sort_values('price', ascending=False).head(10).to_string(index=False))

        print(f"\n=== 5. Статистика по категориям ===")
        by_cat = df.groupby('category')['price'].agg(
            count='count', mean='mean', median='median', std='std'
        ).round(2).sort_values('mean', ascending=False)
        print(by_cat.to_string())

        print(f"\n=== 6. Топ-5 товаров с наибольшим разбросом цен ===")
        spread = df.groupby('product_name')['price'].agg(min='min', max='max').round(2)
        spread['разница'] = spread['max'] - spread['min']
        print(spread.sort_values('разница', ascending=False).head(5).to_string())

    except psycopg2.OperationalError as e:
        print(f" Ошибка подключения: {e}")
        print(" Проверьте host, port, user, password, database")
    except psycopg2.ProgrammingError as e:
        print(f" Ошибка SQL: {e}")
        print(" Проверьте, существуют ли таблицы 'products' и 'prices', и совпадают ли имена колонок")
    except KeyError as e:
        print(f" Отсутствует колонка: {e}. Проверьте SELECT запрос.")
    except Exception as e:
        print(f" Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()