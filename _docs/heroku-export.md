# Heroku Export

## Why?

The Reading Quantified DB (hosted on Heroku) has key info from Trello already parsed & stored in the `books_book` table. The goal is to export this data to CSV.

## Prerequisites

* Heroku CLI
* Postgres (`psql`)

## Commands

Connecting to the DB:

```bash
heroku pg:psql --app reading-quantified-server DATABASE
```

Once connected to the DB:

```sql
--Verify that there are tables
\dt

--Export desired table to CSV (in this case `books_book`)
\COPY books_book TO '_data/heroku.csv' WITH (FORMAT csv, DELIMITER ',',  HEADER true);
```

## References

* [Export a Heroku Postgres table to a csv file](https://jamesbedont.com/export-a-heroku-postgres-table-to-a-csv-file)