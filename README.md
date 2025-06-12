after start of IN0800
in autosys -->  z (enter)
                %checksts.sh_GL0800_2_GLCC_GL_JOBS%

****************************************************************************************************************************

fnsonli password

ssh sutlej

sid
i113racs
export TWO_TASK=i112racd               (because our table is in day)
sid
i112racd

cd /home/fnsonli/GECT
nohup script_for_backup_gect.sh >> $sysout/script_for_backup_gect_20230215&    (EOD date)(Time Taken 5mins)
sqlplus /
select /*+ parallel (GECT,16) full (GECT) */ count(*) from GECT;                                    (GECT Table)

  COUNT(*)
----------
 409070265


select /*+ parallel (GECT_20230215,16) full (GECT_20230215) */ count(*) from GECT_20230215;        (counts should be same)(Backup Table)


  COUNT(*)
----------sid

  409070265 



**************************************************************************************************************************************************

check space in 10.0.20.55 (DB server)
fnsonli password
ssh sutlej
ssh 10.0.20.55
cd  /sbi_bancs/oraarch/i012band/GECT_DUMP_130223
bdf .        (space used should be less than 50%, else rm -Rf .dmp of prev dates)

ctrl d
cd /home/fnsonli/GECT
sid
i112racd

nohup script_for_export_run.sh_NODE5 >> $sysout/script_for_export_run_NODE5_20230215&                     (Time Taken 15mins)
ssh 10.0.20.55
cd  /sbi_bancs/oraarch/i012band/GECT_DUMP_130223
cat GECT_EXPORT_DUMP_20230215.log
Check log file - (no of rows) in export log      (count should match)

53.25 GB 409070265 rows rows

Dump Filename: GECT_20230215_%U.dmp
**************************************************************************************************************************************************
ctrl d
ssh 10.0.20.30
cd /CBS_GECT_DUMP
bdf .        (space used should be less than 50%, else rm -Rf .dmp of prev dates)             

ctrl d
cd /home/fnsonli/GECT
sid
i112racd
./script_for_gect_dump_scp.sh                     (Time Taken 20mins)

After scp Verify exported dumps file size in DB  (10.0.20.55) and GECT DB server(10.0.20.30)
Path - cd /CBS_GECT_DUMP


******************************************************************************************************************************************************

Importing on GECT DB Server
10.0.20.30

   cd $data/file
   cut -c 9-16 MFLAGS
   vim MFLAGS    (change to EOD)

Check space with dba

   Run script_for_import_run.sh in nohup     (in cd $sh)
   nohup script_for_import_run.sh >> $sysout/script_for_import_run_20230215.log &

3) Verify count in GECT_YYYYMMDD in GECTDB and Production table GECT_YYYYMMDD. Count should be same.

sqlplus /

SQL> select /*+ parallel (GECT_20230215,16) full (GECT_20230215) */ count(*) from GECT_20230215;        (EOD)


  COUNT(*)
----------
 409070265



*****************************************************************************************************************************************************

============================ Manual Truncation of GECT ===================================

After completion of POST EOD Backup and Before starting SOD

sutlej
sid
i112racd
sqlplus /

select /*+ parallel (GECT,16) full (GECT) */ count(*) from GECT;                                   

  COUNT(*)
----------
 238258622


exit

cd $sh
sid
i112racd
delete_gect_daily.sh
sqlplus /

select /*+ parallel (GECT,16) full (GECT) */ count(*) from GECT;                                    
                                                                  (Count after truncate should be zero in GECT table.)
  COUNT(*)
----------
         0          

==========================================================================================

**********************************************************************************************************************************************************


Before Start the GECT Offiline loading kindly check var mountpoint if more than 90 tell cdc team to reduce mountpoint


10.0.20.30

For Starting Offline Loading.

confirm Table space with DBA team   (100GB)

mkdir 2022MMDD

Take backup(mv) of GECTIMP_GECT_???.card  from  spool (10.00.20.30) to  /fns/i/r/spool/GECTIMP_GECT_CARD/20230215
--> mv GECTIMP_GECT_???.card /fns/i/r/spool/GECTIMP_GECT_CARD/20230215/.

Card will be eod date -1
Take backup(mv) of 	gect_ranges_*****.card  from  spool (10.00.20.30) to  /fns/i/r/spool/gect_ranges_card
--> mv gect_ranges_*****.card /fns/i/r/spool/gect_ranges_card/.


Take backup(scp) of  /CBS_GECT_DUMP/GECT_IMPORTED_DUMP_20230215.log file to  /fns/i/r/spool/GECT_IMPORTED_DUMP_LOG/20230215
--> scp /CBS_GECT_DUMP/GECT_IMPORTED_DUMP_20230215.log /fns/i/r/spool/GECT_IMPORTED_DUMP_LOG/20230215/.

 Pre checks (Queries) -

run script_for_backup_monitoring_tble.sh   cd $sh


sqlplus /

truncate table mong;
truncate table ldgt;
commit;
exit


>> Run script cd $cat  
 nohup GECTIMP_GECT_LOADER >> $sysout/GECTIMP_GECT_LOADER_20230215.log & 

New GECTIMP_GECT and gect_range cards should be created in spool.

**********************************************************************************************
Monitoring offline loading

INSERTED COUNT:
SELECT SUM(INSERTED),SUM(DELETED),SUM(INSERTED_DUP) FROM MONG;

TOTAL STREAMS:
select count(*) from mong;

STREAMS RUNNING:
SELECT COUNT(*) FROM MONG WHERE STATUS<>'COMPLETED';

SBITFPR:/fns/i/r/sysout:-)cat GECTIMPTOGEMILOADER.LOG

QUERIES RUNNING ON BCKGROUND:
select a.sql_id,b.sql_text from v$session a , v$sql b where a.sql_id=b.sql_id;

After Completion of offline loading
SQL> select count(1) from GECTIMP_20230215;
COUNT(1)
----------
0          
