<p style="text-align:center">
    <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork865-2023-01-01">
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
    </a>
</p>

<h1 align=center><font size = 5>Assignment: SQL Notebook for Peer Assignment</font></h1>

Estimated time needed: **60** minutes.

## Introduction
Using this Python notebook you will:

1.  Understand the Spacex DataSet
2.  Load the dataset  into the corresponding table in a Db2 database
3.  Execute SQL queries to answer assignment questions 


## Overview of the DataSet

SpaceX has gained worldwide attention for a series of historic milestones. 

It is the only private company ever to return a spacecraft from low-earth orbit, which it first accomplished in December 2010.
SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars wheras other providers cost upward of 165 million dollars each, much of the savings is because Space X can reuse the first stage. 


Therefore if we can determine if the first stage will land, we can determine the cost of a launch. 

This information can be used if an alternate company wants to bid against SpaceX for a rocket launch.

This dataset includes a record for each payload carried during a SpaceX mission into outer space.


### Download the datasets

This assignment requires you to load the spacex dataset.

In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. Click on the link below to download and save the dataset (.CSV file):

 <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv" target="_blank">Spacex DataSet</a>



**Navigate to the Go to UI screen** 

* Refer to this insruction in this <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/instructional-labs.md.html">link</a> for viewing  the   Go to UI screen. 


* Later click on **Data link(below SQL)**  in the Go to UI screen  and click on **Load Data** tab.  



* Later browse for the downloaded spacex file.



<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/images/browsefile.png" width="800">


* Once done select the schema andload the file.  


 <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/images/spacexload3.png" width="800">
 



If you are facing a problem in uploading the dataset (which is a csv file), you can follow the steps below to upload the .sql file instead of the CSV file:

* Download the file <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/Spacex%20.sql">Spacex.sql</a>

* Later click on **SQL** in the  **Go to UI Screen**.

* Use the **From file** option to browse for the **SQL** file and upload it.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/images/sqlfile.png">

* Once you upload the script,you can use the **Run All** option to run all the queries to insert the data.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/images/runall.png">

    



```python
# !pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3 
# !pip uninstall ipython-sql -y
# !pip uninstall sqlalchemy==1.4 -y && pip install sqlalchemy==1.3.24
# !pip install ipython-sql==0.4.1
```
 
### Connect to the database

Let us first load the SQL extension and establish a connection with the database



```python
%load_ext sql
```




**DB2 magic in case of  UI service credentials.**



<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/images/servicecredentials.png" width="600">  

* Use the following format.

* Add security=SSL at the end

**%sql ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name?security=SSL**



```python
%sql ibm_db_sa://cgk98202:**********@815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30367/BLUDB?security=SSL
```

## Tasks

Now write and execute SQL queries to solve the assignment tasks.

### Task 1




##### Display the names of the unique launch sites  in the space mission



```sql
%%sql
select * from spacex limit 5;
```

     * ibm_db_sa://cgk98202:***@815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30367/BLUDB
    Done.
    




<table>
    <tr>
        <th>DATE</th>
        <th>time__utc_</th>
        <th>booster_version</th>
        <th>launch_site</th>
        <th>payload</th>
        <th>payload_mass__kg_</th>
        <th>orbit</th>
        <th>customer</th>
        <th>mission_outcome</th>
        <th>landing__outcome</th>
    </tr>
    <tr>
        <td>2010-06-04</td>
        <td>18:45:00</td>
        <td>F9 v1.0  B0003</td>
        <td>CCAFS LC-40</td>
        <td>Dragon Spacecraft Qualification Unit</td>
        <td>0</td>
        <td>LEO</td>
        <td>SpaceX</td>
        <td>Success</td>
        <td>Failure (parachute)</td>
    </tr>
    <tr>
        <td>2010-12-08</td>
        <td>15:43:00</td>
        <td>F9 v1.0  B0004</td>
        <td>CCAFS LC-40</td>
        <td>Dragon demo flight C1, two CubeSats, barrel of Brouere cheese</td>
        <td>0</td>
        <td>LEO (ISS)</td>
        <td>NASA (COTS) NRO</td>
        <td>Success</td>
        <td>Failure (parachute)</td>
    </tr>
    <tr>
        <td>2012-05-22</td>
        <td>07:44:00</td>
        <td>F9 v1.0  B0005</td>
        <td>CCAFS LC-40</td>
        <td>Dragon demo flight C2</td>
        <td>525</td>
        <td>LEO (ISS)</td>
        <td>NASA (COTS)</td>
        <td>Success</td>
        <td>No attempt</td>
    </tr>
    <tr>
        <td>2012-10-08</td>
        <td>00:35:00</td>
        <td>F9 v1.0  B0006</td>
        <td>CCAFS LC-40</td>
        <td>SpaceX CRS-1</td>
        <td>500</td>
        <td>LEO (ISS)</td>
        <td>NASA (CRS)</td>
        <td>Success</td>
        <td>No attempt</td>
    </tr>
    <tr>
        <td>2013-03-01</td>
        <td>15:10:00</td>
        <td>F9 v1.0  B0007</td>
        <td>CCAFS LC-40</td>
        <td>SpaceX CRS-2</td>
        <td>677</td>
        <td>LEO (ISS)</td>
        <td>NASA (CRS)</td>
        <td>Success</td>
        <td>No attempt</td>
    </tr>
</table>




```sql
%%sql
select distinct launch_site from spacex;
```

     * ibm_db_sa://cgk98202:***@815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30367/BLUDB
    Done.
    




<table>
    <tr>
        <th>launch_site</th>
    </tr>
    <tr>
        <td>CCAFS LC-40</td>
    </tr>
    <tr>
        <td>CCAFS SLC-40</td>
    </tr>
    <tr>
        <td>KSC LC-39A</td>
    </tr>
    <tr>
        <td>VAFB SLC-4E</td>
    </tr>
</table>




### Task 2


#####  Display 5 records where launch sites begin with the string 'CCA' 



```sql
%%sql
select * from spacex where launch_site like 'CCA%' limit 5;
```

     * ibm_db_sa://cgk98202:***@815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30367/BLUDB
    Done.
    




<table>
    <tr>
        <th>DATE</th>
        <th>time__utc_</th>
        <th>booster_version</th>
        <th>launch_site</th>
        <th>payload</th>
        <th>payload_mass__kg_</th>
        <th>orbit</th>
        <th>customer</th>
        <th>mission_outcome</th>
        <th>landing__outcome</th>
    </tr>
    <tr>
        <td>2010-06-04</td>
        <td>18:45:00</td>
        <td>F9 v1.0  B0003</td>
        <td>CCAFS LC-40</td>
        <td>Dragon Spacecraft Qualification Unit</td>
        <td>0</td>
        <td>LEO</td>
        <td>SpaceX</td>
        <td>Success</td>
        <td>Failure (parachute)</td>
    </tr>
    <tr>
        <td>2010-12-08</td>
        <td>15:43:00</td>
        <td>F9 v1.0  B0004</td>
        <td>CCAFS LC-40</td>
        <td>Dragon demo flight C1, two CubeSats, barrel of Brouere cheese</td>
        <td>0</td>
        <td>LEO (ISS)</td>
        <td>NASA (COTS) NRO</td>
        <td>Success</td>
        <td>Failure (parachute)</td>
    </tr>
    <tr>
        <td>2012-05-22</td>
        <td>07:44:00</td>
        <td>F9 v1.0  B0005</td>
        <td>CCAFS LC-40</td>
        <td>Dragon demo flight C2</td>
        <td>525</td>
        <td>LEO (ISS)</td>
        <td>NASA (COTS)</td>
        <td>Success</td>
        <td>No attempt</td>
    </tr>
    <tr>
        <td>2012-10-08</td>
        <td>00:35:00</td>
        <td>F9 v1.0  B0006</td>
        <td>CCAFS LC-40</td>
        <td>SpaceX CRS-1</td>
        <td>500</td>
        <td>LEO (ISS)</td>
        <td>NASA (CRS)</td>
        <td>Success</td>
        <td>No attempt</td>
    </tr>
    <tr>
        <td>2013-03-01</td>
        <td>15:10:00</td>
        <td>F9 v1.0  B0007</td>
        <td>CCAFS LC-40</td>
        <td>SpaceX CRS-2</td>
        <td>677</td>
        <td>LEO (ISS)</td>
        <td>NASA (CRS)</td>
        <td>Success</td>
        <td>No attempt</td>
    </tr>
</table>



### Task 3




##### Display the total payload mass carried by boosters launched by NASA (CRS)



```sql
%%sql
select sum(payload_mass__kg_) as total_payload from spacex where customer='NASA (CRS)';
```

     * ibm_db_sa://cgk98202:***@815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30367/BLUDB
    Done.
    




<table>
    <tr>
        <th>total_payload</th>
    </tr>
    <tr>
        <td>45596</td>
    </tr>
</table>



### Task 4




##### Display average payload mass carried by booster version F9 v1.1



```sql
%%sql
select avg(payload_mass__kg_) as average_payload from spacex where booster_version like 'F9 v1.1%';
```

     * ibm_db_sa://cgk98202:***@815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30367/BLUDB
    Done.
    




<table>
    <tr>
        <th>average_payload</th>
    </tr>
    <tr>
        <td>2534</td>
    </tr>
</table>



### Task 5

##### List the date when the first successful landing outcome in ground pad was acheived.


_Hint:Use min function_ 



```sql
%%sql
select min(DATE) as first_success from spacex where landing__outcome='Success (ground pad)';
```

     * ibm_db_sa://cgk98202:***@815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30367/BLUDB
    Done.
    




<table>
    <tr>
        <th>first_success</th>
    </tr>
    <tr>
        <td>2015-12-22</td>
    </tr>
</table>



### Task 6

##### List the names of the boosters which have success in drone ship and have payload mass greater than 4000 but less than 6000



```sql
%%sql
select distinct booster_version from spacex where landing__outcome='Success (drone ship)' and payload_mass__kg_>4000 and payload_mass__kg_<6000;
```

     * ibm_db_sa://cgk98202:***@815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30367/BLUDB
    Done.
    




<table>
    <tr>
        <th>booster_version</th>
    </tr>
    <tr>
        <td>F9 FT  B1021.2</td>
    </tr>
    <tr>
        <td>F9 FT  B1031.2</td>
    </tr>
    <tr>
        <td>F9 FT B1022</td>
    </tr>
    <tr>
        <td>F9 FT B1026</td>
    </tr>
</table>



### Task 7




##### List the total number of successful and failure mission outcomes



```sql
%%sql
select mission_outcome, count(*) as total_number from spacex group by mission_outcome;
```

     * ibm_db_sa://cgk98202:***@815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30367/BLUDB
    Done.
    




<table>
    <tr>
        <th>mission_outcome</th>
        <th>total_number</th>
    </tr>
    <tr>
        <td>Failure (in flight)</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Success</td>
        <td>99</td>
    </tr>
    <tr>
        <td>Success (payload status unclear)</td>
        <td>1</td>
    </tr>
</table>



### Task 8



##### List the   names of the booster_versions which have carried the maximum payload mass. Use a subquery



```sql
%%sql
select distinct booster_version from spacex where payload_mass__kg_ =(select max(payload_mass__kg_) from spacex);
```

     * ibm_db_sa://cgk98202:***@815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30367/BLUDB
    Done.
    




<table>
    <tr>
        <th>booster_version</th>
    </tr>
    <tr>
        <td>F9 B5 B1048.4</td>
    </tr>
    <tr>
        <td>F9 B5 B1048.5</td>
    </tr>
    <tr>
        <td>F9 B5 B1049.4</td>
    </tr>
    <tr>
        <td>F9 B5 B1049.5</td>
    </tr>
    <tr>
        <td>F9 B5 B1049.7</td>
    </tr>
    <tr>
        <td>F9 B5 B1051.3</td>
    </tr>
    <tr>
        <td>F9 B5 B1051.4</td>
    </tr>
    <tr>
        <td>F9 B5 B1051.6</td>
    </tr>
    <tr>
        <td>F9 B5 B1056.4</td>
    </tr>
    <tr>
        <td>F9 B5 B1058.3</td>
    </tr>
    <tr>
        <td>F9 B5 B1060.2</td>
    </tr>
    <tr>
        <td>F9 B5 B1060.3</td>
    </tr>
</table>



### Task 9


##### List the failed landing_outcomes in drone ship, their booster versions, and launch site names for in year 2015



```sql
%%sql
select date, landing__outcome, launch_site, booster_version, customer from spacex where year(date)=2015 and landing__outcome='Failure (drone ship)'
```

     * ibm_db_sa://cgk98202:***@815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30367/BLUDB
    Done.
    




<table>
    <tr>
        <th>DATE</th>
        <th>landing__outcome</th>
        <th>launch_site</th>
        <th>booster_version</th>
        <th>customer</th>
    </tr>
    <tr>
        <td>2015-01-10</td>
        <td>Failure (drone ship)</td>
        <td>CCAFS LC-40</td>
        <td>F9 v1.1 B1012</td>
        <td>NASA (CRS)</td>
    </tr>
    <tr>
        <td>2015-04-14</td>
        <td>Failure (drone ship)</td>
        <td>CCAFS LC-40</td>
        <td>F9 v1.1 B1015</td>
        <td>NASA (CRS)</td>
    </tr>
</table>



### Task 10

##### Rank the count of landing outcomes (such as Failure (drone ship) or Success (ground pad)) between the date 2010-06-04 and 2017-03-20, in descending order



```sql
%%sql
select landing__outcome, count(*) as total from spacex where date between '2010-6-4' and '2017-3-20' group by landing__outcome order by 2 desc
```

     * ibm_db_sa://cgk98202:***@815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30367/BLUDB
    Done.
    




<table>
    <tr>
        <th>landing__outcome</th>
        <th>total</th>
    </tr>
    <tr>
        <td>No attempt</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Failure (drone ship)</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Success (drone ship)</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Controlled (ocean)</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Success (ground pad)</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Failure (parachute)</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Uncontrolled (ocean)</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Precluded (drone ship)</td>
        <td>1</td>
    </tr>
</table>



### Reference Links

* <a href ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20String%20Patterns%20-%20Sorting%20-%20Grouping/instructional-labs.md.html?origin=www.coursera.org">Hands-on Lab : String Patterns, Sorting and Grouping</a>  

*  <a  href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Built-in%20functions%20/Hands-on_Lab__Built-in_Functions.md.html?origin=www.coursera.org">Hands-on Lab: Built-in functions</a>

*  <a  href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sub-queries%20and%20Nested%20SELECTs%20/instructional-labs.md.html?origin=www.coursera.org">Hands-on Lab : Sub-queries and Nested SELECT Statements</a>

*   <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-3-SQLmagic.ipynb">Hands-on Tutorial: Accessing Databases with SQL magic</a>

*  <a href= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-4-Analyzing.ipynb">Hands-on Lab: Analyzing a real World Data Set</a>




## Author(s)

<h4> Lakshmi Holla </h4>


## Other Contributors

<h4> Rav Ahuja </h4>


## Change log
| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2021-10-12 | 0.4 |Lakshmi Holla | Changed markdown|
| 2021-08-24 | 0.3 |Lakshmi Holla | Added library update|
| 2021-07-09 | 0.2 |Lakshmi Holla | Changes made in magic sql|
| 2021-05-20 | 0.1 |Lakshmi Holla | Created Initial Version |


## <h3 align="center"> © IBM Corporation 2021. All rights reserved. <h3/>

