DECLARE @original_url VARCHAR(255) = 'http://www.example.com/';
DECLARE @short_url CHAR(6);
EXECUTE set_url @original_url, @short_url OUTPUT;
SELECT @short_url AS ShortURL;
