BEGIN;
--
-- Create model Applicant
--
CREATE TABLE "jobsearch_applicant" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "education_level" varchar(15) NOT NULL, "resume" varchar(100) NULL);
--
-- Create model Application
--
CREATE TABLE "jobsearch_application" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "resume" varchar(100) NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "status" varchar(20) NOT NULL, "about_yourself" text NULL);
--
-- Create model Company
--
CREATE TABLE "jobsearch_company" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(300) NOT NULL, "region" varchar(30) NOT NULL, "city" varchar(15) NOT NULL, "document" varchar(100) NULL, "description" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "email" varchar(254) NOT NULL, "status" bool NOT NULL);
--
-- Create model Job
--
CREATE TABLE "jobsearch_job" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "start_date" date NOT NULL, "end_date" date NOT NULL, "title" varchar(300) NOT NULL, "description" text NOT NULL, "category" varchar(40) NOT NULL, "requirement" text NOT NULL, "education_level" varchar(15) NOT NULL, "experience" text NOT NULL, "experience_year" integer NOT NULL, "salary" integer NOT NULL, "type" varchar(15) NOT NULL, "region" varchar(30) NOT NULL, "vacancy" integer NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "company_id" bigint NOT NULL REFERENCES "jobsearch_company" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "jobsearch_job_company_id_ecf13394" ON "jobsearch_job" ("company_id");
COMMIT;
