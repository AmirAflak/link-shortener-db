CREATE PROCEDURE prDeleteExpiredUrls
AS
BEGIN
  SET NOCOUNT ON;
  
  DECLARE @currentDate datetime = GETDATE();

  DELETE FROM urls
  WHERE @currentDate > expires_at
END;

