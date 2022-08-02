--ローカルでデータ挿入用のクエリ
CREATE TABLE articles (
 id SERIAL primary key,
 title TEXT NOT NULL,
 author TEXT,
 url TEXT,
 urlToImage TEXT,
 description TEXT,
 country TEXT,
 published_at TEXT,
 updated_at timestamp with time zone default current_timestamp
);

--ローカルでテストデータ挿入用のクエリ
INSERT INTO articles (title, author, url, urlToImage, description, country, published_At) VALUES ('テストタイトル1','テスト著者1','http://localhost/','http://localhost/img','テスト説明1','jp', '2022-08-01T12:41:03Z');