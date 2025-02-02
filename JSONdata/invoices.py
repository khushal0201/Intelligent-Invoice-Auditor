import pandas as pd
from io import StringIO

import pandas as pd
from io import StringIO

invoices=[{
        "id":1,
        "name":"Invoice 1",
        "contract_id":1,
        "status":0,
        "content":"Some invoice content",
        "anomalies":["a","b","c"],
    "employeeData":None
    },
    {
        "id":2,
        "name":"Invoice 2",
        "contract_id":1,
        "status":0,
        "content":"Some invoice content",
        "anomalies":["a","b","c"],
    "employeeData":None
    },
    {
        "id":3,
        "name":"Invoice 3",
        "contract_id":1,
        "status":0,
        "content":"Some invoice content",
        "anomalies":["a","b","c"],
    "employeeData":None
    },
    {
        "id":4,
        "name":"Invoice 4",
        "contract_id":1,
        "status":0,
        "content":"Some invoice content",
        "anomalies":["a","b","c"],
    "employeeData":None
    },
    {
        "id":5,
        "name":"Invoice 5",
        "contract_id":1,
        "status":0,
        "content":"Some invoice content",
        "anomalies":["a","b","c"],
    "employeeData":None
    },
    {
        "id":9,
        "name":"Invoice 9",
        "contract_id":3,
        "status":1,
        "content":"Some invoice content",
        "anomalies":["a","b","c"],
    "employeeData":pd.read_csv(StringIO("""
contractorName,role,projectCode,description,date,hours,rate,amount
Dr. Shawna Schroeder,Quality Assurance Engineer,PRJ005,N/A,2025-01-10T00:00:00.000Z,4,112.0,448.0
Dr. Christie Simonis,Business Analyst,PRJ005,N/A,2024-12-22T00:00:00.000Z,7,127.0,889.0
Mrs. Lisa Kemmer DDS,DevOps Engineer,PRJ002,N/A,2025-01-11T00:00:00.000Z,7,142.0,994.0
Jenny Beahan,Full Stack Developer,PRJ001,N/A,2025-01-12T00:00:00.000Z,8,135.0,1080.0
Forrest Sanford,Project Manager,PRJ005,N/A,2025-01-12T00:00:00.000Z,4,165.0,660.0
Vicki Murphy,Senior Software Architect,PRJ001,N/A,2025-01-12T00:00:00.000Z,4,180.0,720.0
Katie Herman,Full Stack Developer,PRJ003,N/A,2025-01-05T00:00:00.000Z,5,135.0,675.0
Gregory Kuhn,Project Manager,PRJ004,N/A,2025-01-04T00:00:00.000Z,7,165.0,1155.0
Beulah Larkin,UX/UI Designer,PRJ005,N/A,2025-01-08T00:00:00.000Z,7,120.0,840.0
Angel Osinski,Quality Assurance Engineer,PRJ001,N/A,2025-01-01T00:00:00.000Z,8,112.0,896.0
Dr. Kelvin Emmerich,Security Engineer,PRJ002,N/A,2025-01-12T00:00:00.000Z,6,157.0,942.0
Mrs. Rachel Predovic,Technical Writer,PRJ002,N/A,2025-01-05T00:00:00.000Z,7,105.0,735.0
Olivia Brekke-Conn,DevOps Engineer,PRJ002,N/A,2024-12-23T00:00:00.000Z,5,142.0,710.0
Kenny Bradtke,Full Stack Developer,PRJ002,N/A,2024-12-21T00:00:00.000Z,4,135.0,540.0
Jerry Ortiz MD,Quality Assurance Engineer,PRJ001,N/A,2025-01-02T00:00:00.000Z,4,112.0,448.0
Brett Yundt,Project Manager,PRJ003,N/A,2024-12-29T00:00:00.000Z,7,165.0,1155.0
Miss Amy Kuphal,Security Engineer,PRJ003,N/A,2024-12-18T00:00:00.000Z,8,157.0,1256.0
Willard Waters PhD,Project Manager,PRJ002,N/A,2025-01-01T00:00:00.000Z,8,165.0,1320.0
Jeanne Howell,Data Scientist,PRJ004,N/A,2024-12-22T00:00:00.000Z,4,150.0,600.0
Kent Watsica,Project Manager,PRJ001,N/A,2024-12-23T00:00:00.000Z,5,165.0,825.0
Dr. Cody Hyatt,Business Analyst,PRJ003,N/A,2025-01-04T00:00:00.000Z,6,127.0,762.0
Allen Bauch,Security Engineer,PRJ005,N/A,2025-01-08T00:00:00.000Z,6,157.0,942.0
Glenda Macejkovic,Technical Writer,PRJ003,N/A,2024-12-27T00:00:00.000Z,7,105.0,735.0
Terrance Hansen,Business Analyst,PRJ003,N/A,2025-01-02T00:00:00.000Z,6,127.0,762.0
Brandon Mayert Sr.,UX/UI Designer,PRJ004,N/A,2024-12-19T00:00:00.000Z,7,120.0,840.0
Jerald Weissnat,Security Engineer,PRJ002,N/A,2024-12-29T00:00:00.000Z,6,157.0,942.0
Winifred Graham,Data Scientist,PRJ004,N/A,2024-12-23T00:00:00.000Z,6,150.0,900.0
Alison Corwin,UX/UI Designer,PRJ002,N/A,2025-01-03T00:00:00.000Z,8,120.0,960.0
Diana Mayer-Gislason,Senior Software Architect,PRJ004,N/A,2024-12-27T00:00:00.000Z,8,180.0,1440.0
Carol Murphy,Quality Assurance Engineer,PRJ001,N/A,2024-12-30T00:00:00.000Z,5,112.0,560.0
Mack Lockman,Security Engineer,PRJ001,N/A,2025-01-12T00:00:00.000Z,6,157.0,942.0
Mrs. Yolanda Hoeger DDS,Quality Assurance Engineer,PRJ001,N/A,2024-12-26T00:00:00.000Z,4,112.0,448.0
Jaime Aufderhar,DevOps Engineer,PRJ005,N/A,2024-12-21T00:00:00.000Z,5,142.0,710.0
Leslie Windler,Quality Assurance Engineer,PRJ004,N/A,2025-01-01T00:00:00.000Z,6,112.0,672.0
Lyle Runolfsson DDS,Project Manager,PRJ001,N/A,2025-01-06T00:00:00.000Z,7,165.0,1155.0
Hubert Ward,Senior Software Architect,PRJ005,N/A,2024-12-30T00:00:00.000Z,4,180.0,720.0
Julio Casper,Senior Software Architect,PRJ005,N/A,2025-01-11T00:00:00.000Z,6,180.0,1080.0
Ms. Joann Anderson,Data Scientist,PRJ002,N/A,2025-01-10T00:00:00.000Z,4,150.0,600.0
Eleanor Gutkowski,Business Analyst,PRJ004,N/A,2025-01-09T00:00:00.000Z,6,127.0,762.0
Nancy Ziemann,Security Engineer,PRJ002,N/A,2025-01-03T00:00:00.000Z,7,157.0,1099.0
Ellis Mraz,Senior Software Architect,PRJ004,N/A,2024-12-30T00:00:00.000Z,8,180.0,1440.0
Marie Flatley,Full Stack Developer,PRJ003,N/A,2025-01-07T00:00:00.000Z,4,135.0,540.0
Dale Turcotte,Technical Writer,PRJ003,N/A,2024-12-27T00:00:00.000Z,8,105.0,840.0
Krystal Rowe,Security Engineer,PRJ003,N/A,2024-12-26T00:00:00.000Z,8,157.0,1256.0
Tony Zboncak,UX/UI Designer,PRJ002,N/A,2025-01-13T00:00:00.000Z,5,120.0,600.0
Orlando Hansen,Project Manager,PRJ003,N/A,2025-01-05T00:00:00.000Z,7,165.0,1155.0
Teresa Padberg Sr.,Project Manager,PRJ001,N/A,2025-01-13T00:00:00.000Z,4,165.0,660.0
Kelly Hoeger-Doyle,Full Stack Developer,PRJ001,N/A,2025-01-11T00:00:00.000Z,4,135.0,540.0
Mr. Lonnie Botsford,Project Manager,PRJ001,N/A,2024-12-16T00:00:00.000Z,7,165.0,1155.0
Alfonso Abbott,UX/UI Designer,PRJ001,N/A,2025-01-13T00:00:00.000Z,4,120.0,480.0
Ms. Faith Gorczany,DevOps Engineer,PRJ004,N/A,2024-12-15T00:00:00.000Z,4,142.0,568.0
Phillip Crist,Business Analyst,PRJ004,N/A,2025-01-13T00:00:00.000Z,8,127.0,1016.0
Brandi Wolf,Project Manager,PRJ004,N/A,2024-12-17T00:00:00.000Z,8,165.0,1320.0
Mrs. Gail Ebert,Data Scientist,PRJ001,N/A,2025-01-06T00:00:00.000Z,7,150.0,1050.0
Dr. Edmund Mertz Sr.,UX/UI Designer,PRJ001,N/A,2025-01-01T00:00:00.000Z,4,120.0,480.0
Frank Littel,Project Manager,PRJ001,N/A,2024-12-31T00:00:00.000Z,4,165.0,660.0
Hubert Carroll-Jaskolski DVM,Technical Writer,PRJ004,N/A,2024-12-26T00:00:00.000Z,5,105.0,525.0
Leland Franey,Project Manager,PRJ003,N/A,2025-01-05T00:00:00.000Z,4,165.0,660.0
Dr. Merle Maggio,Project Manager,PRJ004,N/A,2025-01-10T00:00:00.000Z,4,165.0,660.0
Nina Ryan-Daniel,Technical Writer,PRJ005,N/A,2024-12-16T00:00:00.000Z,5,105.0,525.0
Rudolph Bogan-Pacocha II,DevOps Engineer,PRJ005,N/A,2024-12-29T00:00:00.000Z,6,142.0,852.0
Nicholas Treutel,Technical Writer,PRJ001,N/A,2025-01-11T00:00:00.000Z,7,105.0,735.0
Casey Rempel,Full Stack Developer,PRJ004,N/A,2024-12-25T00:00:00.000Z,8,135.0,1080.0
Lowell Bailey,Data Scientist,PRJ004,N/A,2025-01-02T00:00:00.000Z,4,150.0,600.0
Troy Pollich I,Security Engineer,PRJ001,N/A,2025-01-13T00:00:00.000Z,6,157.0,942.0
Gretchen Moen,Quality Assurance Engineer,PRJ002,N/A,2025-01-12T00:00:00.000Z,5,112.0,560.0
Shelia Metz,Quality Assurance Engineer,PRJ003,N/A,2025-01-04T00:00:00.000Z,4,112.0,448.0
Nelson Cronin,Technical Writer,PRJ005,N/A,2024-12-26T00:00:00.000Z,5,105.0,525.0
Leon Jacobi,Business Analyst,PRJ001,N/A,2025-01-06T00:00:00.000Z,8,127.0,1016.0
Beverly Armstrong,UX/UI Designer,PRJ002,N/A,2025-01-02T00:00:00.000Z,8,120.0,960.0
Lucille Gusikowski,Technical Writer,PRJ005,N/A,2025-01-03T00:00:00.000Z,6,105.0,630.0
"""))
    },
{
        "id":5,
        "name":"Invoice 903",
        "contract_id":3,
        "status":1,
        "content":"Some invoice content",
        "anomalies":["a","b","c"],
    "employeeData":pd.read_csv(StringIO("""
contractorName,role,projectCode,description,date,hours,rate,amount
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2025-01-04T00:00:00.000Z,6,142.0,852.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-19T00:00:00.000Z,6,157.0,942.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-23T00:00:00.000Z,4,105.0,420.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-19T00:00:00.000Z,4,157.0,628.0
Herman Frami DDS,DevOps Engineer,PRJ001,N/A,2025-01-09T00:00:00.000Z,8,165.0,1320.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2024-12-17T00:00:00.000Z,8,135.0,1080.0
Herman Frami DDS,DevOps Engineer,PRJ005,N/A,2025-01-05T00:00:00.000Z,4,142.0,568.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2025-01-04T00:00:00.000Z,6,150.0,900.0
Herman Frami DDS,DevOps Engineer,PRJ001,N/A,2025-01-14T00:00:00.000Z,6,135.0,810.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2024-12-30T00:00:00.000Z,6,120.0,720.0
Herman Frami DDS,DevOps Engineer,PRJ001,N/A,2025-01-10T00:00:00.000Z,8,157.0,1256.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2024-12-19T00:00:00.000Z,7,135.0,945.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-28T00:00:00.000Z,5,165.0,825.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2025-01-13T00:00:00.000Z,8,165.0,1320.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2025-01-08T00:00:00.000Z,8,105.0,840.0
Herman Frami DDS,DevOps Engineer,PRJ005,N/A,2024-12-17T00:00:00.000Z,7,180.0,1260.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-21T00:00:00.000Z,6,165.0,990.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2024-12-23T00:00:00.000Z,8,150.0,1200.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-26T00:00:00.000Z,8,127.0,1016.0
Herman Frami DDS,DevOps Engineer,PRJ001,N/A,2025-01-09T00:00:00.000Z,7,180.0,1260.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2025-01-08T00:00:00.000Z,8,112.0,896.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2025-01-13T00:00:00.000Z,4,127.0,508.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2025-01-07T00:00:00.000Z,5,112.0,560.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2024-12-24T00:00:00.000Z,4,165.0,660.0
Herman Frami DDS,DevOps Engineer,PRJ001,N/A,2024-12-26T00:00:00.000Z,6,180.0,1080.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-19T00:00:00.000Z,7,135.0,945.0
Herman Frami DDS,DevOps Engineer,PRJ001,N/A,2024-12-22T00:00:00.000Z,7,135.0,945.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2024-12-16T00:00:00.000Z,8,157.0,1256.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2025-01-13T00:00:00.000Z,7,120.0,840.0
Herman Frami DDS,DevOps Engineer,PRJ005,N/A,2025-01-10T00:00:00.000Z,6,105.0,630.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2025-01-06T00:00:00.000Z,7,180.0,1260.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2024-12-30T00:00:00.000Z,5,105.0,525.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-16T00:00:00.000Z,6,120.0,720.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2025-01-11T00:00:00.000Z,7,150.0,1050.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2024-12-30T00:00:00.000Z,7,180.0,1260.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2025-01-07T00:00:00.000Z,8,165.0,1320.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2024-12-19T00:00:00.000Z,5,142.0,710.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2024-12-22T00:00:00.000Z,5,142.0,710.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-23T00:00:00.000Z,7,112.0,784.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-22T00:00:00.000Z,7,142.0,994.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2025-01-11T00:00:00.000Z,5,165.0,825.0
Herman Frami DDS,DevOps Engineer,PRJ005,N/A,2024-12-17T00:00:00.000Z,4,180.0,720.0
Herman Frami DDS,DevOps Engineer,PRJ005,N/A,2025-01-09T00:00:00.000Z,4,127.0,508.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-25T00:00:00.000Z,7,105.0,735.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2024-12-16T00:00:00.000Z,7,165.0,1155.0
Herman Frami DDS,DevOps Engineer,PRJ005,N/A,2024-12-22T00:00:00.000Z,6,165.0,990.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2024-12-16T00:00:00.000Z,7,127.0,889.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2024-12-19T00:00:00.000Z,5,112.0,560.0
Herman Frami DDS,DevOps Engineer,PRJ005,N/A,2024-12-30T00:00:00.000Z,5,180.0,900.0
Herman Frami DDS,DevOps Engineer,PRJ001,N/A,2024-12-26T00:00:00.000Z,7,180.0,1260.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-23T00:00:00.000Z,8,120.0,960.0
Herman Frami DDS,DevOps Engineer,PRJ005,N/A,2024-12-18T00:00:00.000Z,8,157.0,1256.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2024-12-18T00:00:00.000Z,6,105.0,630.0
Herman Frami DDS,DevOps Engineer,PRJ005,N/A,2025-01-05T00:00:00.000Z,7,165.0,1155.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2024-12-18T00:00:00.000Z,8,120.0,960.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-23T00:00:00.000Z,6,142.0,852.0
Herman Frami DDS,DevOps Engineer,PRJ001,N/A,2024-12-28T00:00:00.000Z,6,157.0,942.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2025-01-02T00:00:00.000Z,7,120.0,840.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2025-01-13T00:00:00.000Z,8,127.0,1016.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-28T00:00:00.000Z,5,105.0,525.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2024-12-27T00:00:00.000Z,7,120.0,840.0
Herman Frami DDS,DevOps Engineer,PRJ001,N/A,2025-01-12T00:00:00.000Z,4,150.0,600.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2025-01-05T00:00:00.000Z,5,142.0,710.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2025-01-09T00:00:00.000Z,6,180.0,1080.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2024-12-23T00:00:00.000Z,5,180.0,900.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2025-01-12T00:00:00.000Z,8,180.0,1440.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2025-01-10T00:00:00.000Z,6,180.0,1080.0
Herman Frami DDS,DevOps Engineer,PRJ001,N/A,2025-01-01T00:00:00.000Z,4,120.0,480.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2024-12-23T00:00:00.000Z,8,180.0,1440.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2025-01-01T00:00:00.000Z,4,165.0,660.0
Herman Frami DDS,DevOps Engineer,PRJ005,N/A,2025-01-11T00:00:00.000Z,8,127.0,1016.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2024-12-22T00:00:00.000Z,6,112.0,672.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2024-12-30T00:00:00.000Z,8,180.0,1440.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-31T00:00:00.000Z,7,112.0,784.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2025-01-12T00:00:00.000Z,7,180.0,1260.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2024-12-29T00:00:00.000Z,8,180.0,1440.0
Herman Frami DDS,DevOps Engineer,PRJ001,N/A,2024-12-17T00:00:00.000Z,8,135.0,1080.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2025-01-09T00:00:00.000Z,4,112.0,448.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2025-01-07T00:00:00.000Z,7,157.0,1099.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2025-01-13T00:00:00.000Z,7,135.0,945.0
Herman Frami DDS,DevOps Engineer,PRJ001,N/A,2024-12-25T00:00:00.000Z,4,135.0,540.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2024-12-21T00:00:00.000Z,7,135.0,945.0
Herman Frami DDS,DevOps Engineer,PRJ001,N/A,2024-12-23T00:00:00.000Z,5,112.0,560.0
Herman Frami DDS,DevOps Engineer,PRJ001,N/A,2024-12-17T00:00:00.000Z,7,112.0,784.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-26T00:00:00.000Z,5,165.0,825.0
Herman Frami DDS,DevOps Engineer,PRJ004,N/A,2024-12-21T00:00:00.000Z,4,150.0,600.0
Herman Frami DDS,DevOps Engineer,PRJ003,N/A,2024-12-29T00:00:00.000Z,5,157.0,785.0
Herman Frami DDS,DevOps Engineer,PRJ001,N/A,2025-01-13T00:00:00.000Z,5,180.0,900.0
Herman Frami DDS,DevOps Engineer,PRJ001,N/A,2024-12-17T00:00:00.000Z,8,157.0,1256.0
Herman Frami DDS,DevOps Engineer,PRJ002,N/A,2024-12-18T00:00:00.000Z,6,127.0,762.0
Jackie Wiegand,Quality Assurance Engineer,PRJ002,N/A,2024-12-22T00:00:00.000Z,4,112.0,448.0
Jackie Wiegand,Quality Assurance Engineer,PRJ005,N/A,2024-12-31T00:00:00.000Z,7,127.0,889.0
Jackie Wiegand,Quality Assurance Engineer,PRJ003,N/A,2024-12-17T00:00:00.000Z,6,135.0,810.0
Jackie Wiegand,Quality Assurance Engineer,PRJ002,N/A,2024-12-19T00:00:00.000Z,7,165.0,1155.0
Jackie Wiegand,Quality Assurance Engineer,PRJ005,N/A,2025-01-13T00:00:00.000Z,6,180.0,1080.0
Jackie Wiegand,Quality Assurance Engineer,PRJ004,N/A,2024-12-16T00:00:00.000Z,7,142.0,994.0
Jackie Wiegand,Quality Assurance Engineer,PRJ003,N/A,2024-12-21T00:00:00.000Z,7,150.0,1050.0
Jackie Wiegand,Quality Assurance Engineer,PRJ001,N/A,2025-01-10T00:00:00.000Z,8,120.0,960.0
Dianna Stehr,DevOps Engineer,PRJ002,N/A,2025-01-06T00:00:00.000Z,5,142.0,710.0
Dianna Stehr,DevOps Engineer,PRJ001,N/A,2024-12-28T00:00:00.000Z,7,157.0,1099.0
Dianna Stehr,DevOps Engineer,PRJ003,N/A,2024-12-30T00:00:00.000Z,4,142.0,568.0
Dianna Stehr,DevOps Engineer,PRJ002,N/A,2024-12-25T00:00:00.000Z,7,120.0,840.0
Dianna Stehr,DevOps Engineer,PRJ005,N/A,2025-01-02T00:00:00.000Z,5,165.0,825.0
Dianna Stehr,DevOps Engineer,PRJ002,N/A,2025-01-12T00:00:00.000Z,7,135.0,945.0
Dianna Stehr,DevOps Engineer,PRJ003,N/A,2025-01-08T00:00:00.000Z,6,150.0,900.0
Dianna Stehr,DevOps Engineer,PRJ001,N/A,2024-12-16T00:00:00.000Z,5,142.0,710.0
Dianna Stehr,DevOps Engineer,PRJ001,N/A,2024-12-21T00:00:00.000Z,7,127.0,889.0
Dianna Stehr,DevOps Engineer,PRJ001,N/A,2025-01-07T00:00:00.000Z,5,150.0,750.0
Dianna Stehr,DevOps Engineer,PRJ001,N/A,2024-12-28T00:00:00.000Z,4,150.0,600.0
Dianna Stehr,DevOps Engineer,PRJ004,N/A,2024-12-29T00:00:00.000Z,5,135.0,675.0
Dianna Stehr,DevOps Engineer,PRJ002,N/A,2025-01-01T00:00:00.000Z,6,120.0,720.0
Dianna Stehr,DevOps Engineer,PRJ002,N/A,2025-01-07T00:00:00.000Z,7,157.0,1099.0
Dianna Stehr,DevOps Engineer,PRJ005,N/A,2024-12-16T00:00:00.000Z,8,157.0,1256.0
Dianna Stehr,DevOps Engineer,PRJ002,N/A,2024-12-23T00:00:00.000Z,4,157.0,628.0
Dianna Stehr,DevOps Engineer,PRJ003,N/A,2024-12-24T00:00:00.000Z,5,135.0,675.0
Dianna Stehr,DevOps Engineer,PRJ004,N/A,2024-12-21T00:00:00.000Z,5,112.0,560.0
Dianna Stehr,DevOps Engineer,PRJ005,N/A,2025-01-06T00:00:00.000Z,6,180.0,1080.0
Dianna Stehr,DevOps Engineer,PRJ004,N/A,2024-12-19T00:00:00.000Z,4,142.0,568.0
Dianna Stehr,DevOps Engineer,PRJ004,N/A,2024-12-24T00:00:00.000Z,6,105.0,630.0
Dianna Stehr,DevOps Engineer,PRJ005,N/A,2024-12-17T00:00:00.000Z,8,150.0,1200.0
"""))
    },
]
