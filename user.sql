BEGIN;
--
-- Create model User
--
CREATE TABLE "user_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "gender" varchar(2) NOT NULL, "phone" varchar(13) NOT NULL, "region" varchar(30) NOT NULL, "city" varchar(15) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "user_type" varchar(20) NOT NULL);
CREATE TABLE "user_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" bigint NOT NULL REFERENCES "user_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "user_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" bigint NOT NULL REFERENCES "user_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "user_user_groups_user_id_group_id_bb60391f_uniq" ON "user_user_groups" ("user_id", "group_id");
CREATE INDEX "user_user_groups_user_id_13f9a20d" ON "user_user_groups" ("user_id");
CREATE INDEX "user_user_groups_group_id_c57f13c0" ON "user_user_groups" ("group_id");
CREATE UNIQUE INDEX "user_user_user_permissions_user_id_permission_id_64f4d5b8_uniq" ON "user_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "user_user_user_permissions_user_id_31782f58" ON "user_user_user_permissions" ("user_id");
CREATE INDEX "user_user_user_permissions_permission_id_ce49d4de" ON "user_user_user_permissions" ("permission_id");
COMMIT;
