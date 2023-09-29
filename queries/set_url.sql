CREATE PROCEDURE set_url
    @original_url VARCHAR(255),
	@short_url CHAR(6) OUTPUT
AS
BEGIN
	DECLARE @exists int;

	-- check if original_url already exists
	SELECT @exists = COUNT(*) FROM urls WHERE original_url = @original_url;

	IF @exists > 0
	BEGIN
		-- original_url already exists, return existing short_url
		SELECT short_url FROM urls WHERE original_url = @original_url;
	END
	ELSE
	BEGIN
		SET @short_url = LOWER(LEFT(CONVERT(VARCHAR(50), NEWID()), 6));

		WHILE EXISTS (SELECT 1 FROM urls WHERE short_url = @short_url)
		BEGIN
			-- Short URL already exists, generate a new one
			SET @short_url = LOWER(LEFT(CONVERT(VARCHAR(50), NEWID()), 6))
		END

		INSERT INTO urls (short_url, original_url, num_referrals, created_at, last_referenced_at, expires_at)
		VALUES (@short_url, @original_url, 0, GETDATE(), NULL, DATEADD(minute, 1, GETDATE()));

	END
END




