query_creacion_bbdd = "CREATE SCHEMA abc_corporation;"

query_personal_employee = """CREATE TABLE personal_employee (
                            employeenumber INT NOT NULL, 
                            age INT DEFAULT NULL,
                            datebirth VARCHAR(50),
                            gender VARCHAR(50),
                            maritalstatus VARCHAR(250),
                            education INT DEFAULT NULL,
                            educationfield VARCHAR(250),
                            PRIMARY KEY (employeenumber));
                        """

query_job_data = """CREATE TABLE job_data (
                    employeenumber INT NOT NULL,
                    dailyrate INT,
                    monthlyincome INT,
                    monthlyrate INT,
                    percentsalaryhike INT,
                    hourlyrate INT,
                    jobrole VARCHAR(250),
                    joblevel INT,
                    totalworkingyears INT,
                    trainingtimeslastyear INT,
                    yearsatcompany INT,
                    yearssincelastpromotion INT,
                    yearswithcurrmanager INT,
                    remotework VARCHAR(100),
                    stockoptionlevel INT,
                    performancerating INT);
                    """

query_job_satisfaction = """CREATE TABLE job_satisfaction (
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
                        overtime VARCHAR(250));
                        """

query_insertar_employee = "INSERT INTO personal_employee (employeenumber, age, education, educationfield, gender, maritalstatus, datebirth) VALUES (%s, %s, %s, %s, %s, %s, %s)"

query_insertar_job_satisfaction = """
    INSERT INTO job_satisfaction (employeenumber, attrition, businesstravel, distancefromhome, environmentsatisfaction,
                                   jobinvolvement, jobsatisfaction, numcompaniesworked, overtime, relationshipsatisfaction, worklifebalance)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

query_insertar_job_data = """
    INSERT INTO job_data (employeenumber, dailyrate, hourlyrate, joblevel, jobrole, monthlyincome, monthlyrate, percentsalaryhike,
                          performancerating, stockoptionlevel, totalworkingyears, trainingtimeslastyear, yearsatcompany, yearssincelastpromotion,
                          yearswithcurrmanager, remotework)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


