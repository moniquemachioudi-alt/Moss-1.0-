-- ================================================================================
-- Moss database schema v1
-- To run in the Supabase SQL Editor

-- Order matters: A table must exist before another ytable can reference it. 
-- So the order is users -> plants -> devices -> readings 
-- ================================================================================

-- When a database is initialized you want to remove anything that may have 
-- existed before to prevent data contamination 
DROP TABLE IF EXISTS readings CASCADE; 
DROP TABLE IF EXISTS devices CASCASE; 
DROP TABLE IF EXISTS plants CASCADE; 
DROP TABLE IF EXISTS users CASCADE; 

-- ========================================================================
-- USERS: one row per person who logins 
-- ========================================================================

CREATE TABLE users (
    user_id text primary key, 
    username text,
    email text 
);

-- ========================================================================
-- PLANTS: one row per type of plant for a specific user 
-- ========================================================================

CREATE TABLE plants (
    plant_id uuid primary key deafult gen_random_uuid(), 
    plant_category text, 
    plant_type text, 
    -- REMOVED NOT NULL FROM THE COLUMNS FOR NOW BECASE WE ARE STILL TRYING TO 
    -- INTEGRATE ALL THE COMPONENTS 
    reading_baseline_min_soil_moisture real, 
    reading_baseline_max_soil_moisture real,
    reading_baseline_min_water_humidity real,
    reading_baseline_max_water_humidity real,
    reading_baseline_min_sunlight real,
    reading_baseline_max_sunlight real,
    reading_baseline_min_soil_air_temperature real,
    reading_baseline_max_soil_air_temperature real,
    user_id text references users(user_id)
);

-- ========================================================================
-- DEVICES: one row per device for a specific user, plant
-- ========================================================================

CREATE TABLE devices (
    esp32_id_number text primary key,
    location text,
    active_nonactive boolean not null,
    plant_id uuid references plants(plant_id),
    user_id text references users(user_id)
);
-- ========================================================================
-- READINGS: one row per reading for a specific plant, device 
-- ========================================================================

CREATE TABLE readings (
    device_id text not null references devices(esp32_id_number),
    recorded_at timestamptz not null default now(),
    readings_raw real,
    readings_converted real,
    plant_id uuid references plants(plant_id),
    primary key (device_id, recorded_at)

);


ALTER TABLE  users ENABLE ROW LEVEL SECURITY;
ALTER TABLE plants ENABLE ROW LEVEL SECURITY;
ALTER TABLE devices ENABLE ROW LEVEL SECURITY;
ALTER TABLE readings ENABLE ROW LEVEL SECURITY;