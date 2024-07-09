CREATE SCHEMA abc_corporation;
USE abc_corporation;
CREATE TABLE personal_employee (
    employeenumber INT NOT NULL, 
    age INT DEFAULT NULL,
    datebirth VARCHAR(50),
    gender VARCHAR(50),
    maritalstatus VARCHAR(250),
    education INT DEFAULT NULL,
    educationfield VARCHAR(250),
    PRIMARY KEY (employeenumber)
);

CREATE TABLE job_data (
    employeenumber INT NOT NULL,
    dailyrate INT,
    monthlyincome INT,
    monthlyrate INT,
    percentsalaryhike INT,
    hourlyrate INT,
    jobrole VARCHAR(250),
    joblevel INT,
    totalworkingyears INT,
    trainingtimelastyear INT,
    yearsatcompany INT,
    yearssincelastpromotion INT,
    yearswithcurrmanager INT,
    remotework VARCHAR(100),
    stockoptionlevel INT,
    performancerating INT
);

CREATE TABLE job_satisfaction (
    employeenumber INT NOT NULL,
    jobinvolvement VARCHAR(250),
    jobsatisfaction INT,
    businesstravel VARCHAR(250),
    distancefromhome INT, 
    environmentsatisfaction INT,
    relationshipsatisfaction INT,
    worklifebalance INT,
    attrition VARCHAR(250),
    numcompaniesworked INT,
    overtime VARCHAR(250)
);