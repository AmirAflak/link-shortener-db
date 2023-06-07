CREATE PROCEDURE create_urls_table
AS
BEGIN
    SET NOCOUNT ON;

    IF OBJECT_ID('urls', 'U') IS NOT NULL
    BEGIN
        DROP TABLE urls
    END;

    CREATE TABLE urls(
        short_url CHAR(6) PRIMARY KEY,
        original_url VARCHAR(255), 
        num_referrals INT,
        created_at DATETIME,
        last_referenced_at DATETIME,
        expires_at DATETIME
    );
END

