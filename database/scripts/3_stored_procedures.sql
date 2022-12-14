USE [master]
GO
/****** Object:  StoredProcedure [dbo].[AllBeneficiaries]    Script Date: 04/11/2022 12:11:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[AllBeneficiaries]
    @employee_id INT
AS
SELECT 
    b.*,
    n.description 'nationality'
FROM dbo.beneficiaries b
INNER JOIN dbo.employees e ON
    e.id = b.employee_id AND
    e.is_active = 1
INNER JOIN dbo.nationalities n ON
    n.id = b.nationality_id
WHERE b.employee_id = @employee_id AND b.is_active = 1 AND e.is_active = 1;
GO
/****** Object:  StoredProcedure [dbo].[AllEmployees]    Script Date: 04/11/2022 12:11:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[AllEmployees]
AS
SELECT 
    e.*,
    n.description 'nationality'
FROM dbo.employees e
INNER JOIN dbo.nationalities n on
    n.id = e.nationality_id
WHERE e.is_active = 1;
GO
/****** Object:  StoredProcedure [dbo].[AllNationalities]    Script Date: 04/11/2022 12:11:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[AllNationalities]
AS
SELECT * FROM dbo.nationalities
GO
/****** Object:  StoredProcedure [dbo].[GetAdmin]    Script Date: 04/11/2022 12:11:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[GetAdmin]
    @id INT
AS
SELECT * FROM dbo.admins WHERE id = @id
GO
/****** Object:  StoredProcedure [dbo].[GetAdminByUsername]    Script Date: 04/11/2022 12:11:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[GetAdminByUsername]
    @username VARCHAR (50)
AS
SELECT * FROM dbo.admins WHERE username = @username
GO
/****** Object:  StoredProcedure [dbo].[GetBeneficiary]    Script Date: 04/11/2022 12:11:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[GetBeneficiary]
    @id INT,
    @employee_id INT
AS
SELECT 
    b.*,
    n.description 'nationality'
FROM dbo.beneficiaries b
INNER JOIN dbo.employees e ON
    e.id = b.employee_id AND
    e.is_active = 1
INNER JOIN dbo.nationalities n ON
    n.id = b.nationality_id
WHERE b.id = @id AND b.employee_id = @employee_id AND b.is_active = 1 AND e.is_active = 1;
GO
/****** Object:  StoredProcedure [dbo].[GetEmployee]    Script Date: 04/11/2022 12:11:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[GetEmployee]
    @id INT
AS
SELECT 
    e.*,
    n.description 'nationality'
FROM dbo.employees e
INNER JOIN dbo.nationalities n on
    n.id = e.nationality_id
WHERE e.id = @id AND e.is_active = 1;
GO
/****** Object:  StoredProcedure [dbo].[GetNationality]    Script Date: 04/11/2022 12:11:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[GetNationality]
    @id INT
AS
SELECT * FROM dbo.nationalities WHERE id = @id
GO
/****** Object:  StoredProcedure [dbo].[InsertBeneficiary]    Script Date: 04/11/2022 12:11:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[InsertBeneficiary]
    @nationality_id INT,
    @employee_id INT,
    @first_name VARCHAR (50),
    @last_name VARCHAR (50),
    @birth_date DATE,
    @curp VARCHAR (18),
    @ssn VARCHAR (9),
    @phone VARCHAR (10),
    @participation_percent NUMERIC (5, 2)
AS
INSERT INTO dbo.beneficiaries (
    nationality_id,
    employee_id,
    first_name,
    last_name,
    birth_date,
    curp,
    ssn,
    phone,
    participation_percent
) 
OUTPUT INSERTED.*
VALUES (
    @nationality_id,
    @employee_id,
    @first_name,
    @last_name,
    @birth_date,
    @curp,
    @ssn,
    @phone,
    @participation_percent
)
GO
/****** Object:  StoredProcedure [dbo].[InsertEmployee]    Script Date: 04/11/2022 12:11:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[InsertEmployee]
    @nationality_id INT,
    @first_name VARCHAR (50),
    @last_name VARCHAR (50),
    @birth_date DATE,
    @employee_number VARCHAR (10),
    @curp VARCHAR (18),
    @ssn VARCHAR (9),
    @phone VARCHAR (10)
AS
INSERT INTO dbo.employees (
    nationality_id,
    first_name,
    last_name,
    birth_date,
    employee_number,
    curp,
    ssn,
    phone
) 
OUTPUT INSERTED.*
VALUES (
    @nationality_id,
    @first_name,
    @last_name,
    @birth_date,
    @employee_number,
    @curp,
    @ssn,
    @phone
)
GO
/****** Object:  StoredProcedure [dbo].[UpdateBeneficiary]    Script Date: 04/11/2022 12:11:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[UpdateBeneficiary]
    @id INT,
    @nationality_id INT,
    @employee_id INT,
    @first_name VARCHAR (50),
    @last_name VARCHAR (50),
    @birth_date DATE,
    @curp VARCHAR (18),
    @ssn VARCHAR (9),
    @phone VARCHAR (10),
    @participation_percent NUMERIC (5, 2),
    @is_active BIT
AS
UPDATE dbo.beneficiaries
SET
    nationality_id = @nationality_id,
    first_name = @first_name,
    last_name = @last_name,
    birth_date = @birth_date,
    curp = @curp,
    ssn = @ssn,
    phone = @phone,
    participation_percent = @participation_percent,
    is_active = @is_active
OUTPUT INSERTED.*
WHERE
    id = @id AND
    employee_id = @employee_id
GO
/****** Object:  StoredProcedure [dbo].[UpdateEmployee]    Script Date: 04/11/2022 12:11:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[UpdateEmployee]
    @id INT,
    @nationality_id INT,
    @first_name VARCHAR (50),
    @last_name VARCHAR (50),
    @birth_date DATE,
    @employee_number VARCHAR (10),
    @curp VARCHAR (18),
    @ssn VARCHAR (9),
    @phone VARCHAR (10),
    @is_active BIT
AS
UPDATE dbo.employees
SET
    nationality_id = @nationality_id,
    first_name = @first_name,
    last_name = @last_name,
    birth_date = @birth_date,
    employee_number = @employee_number,
    curp = @curp,
    ssn = @ssn,
    phone = @phone,
    is_active = @is_active
OUTPUT INSERTED.*
WHERE
    id = @id
GO
