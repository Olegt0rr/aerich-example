-- upgrade --
ALTER TABLE "user" ADD "last_name" VARCHAR(64) NOT NULL;
-- downgrade --
ALTER TABLE "user" DROP COLUMN "last_name";
