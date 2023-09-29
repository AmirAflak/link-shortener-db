INSERT INTO urls (short_url, original_url, num_referrals, created_at, last_referenced_at)
VALUES 
	('abc123', 'https://www.example.com/page1', 0, GETDATE(), NULL),
	('def456', 'https://www.example.com/page2', 0, GETDATE(), NULL),
	('ghi789', 'https://www.example.com/page3', 0, GETDATE(), NULL),
	('jkl012', 'https://www.example.com/page4', 0, GETDATE(), NULL);

SELECT * FROM URLS;