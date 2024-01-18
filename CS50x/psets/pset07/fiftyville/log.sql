-- Keep a log of any SQL queries you execute as you solve the mystery.

-- All you know is that the theft took place on July 28, 2021 and that it took place on Humphrey Street.

-- Read the report of the crime scene
.tables
.schema crime_scene_reports
SELECT * FROM crime_scene_reports WHERE day = 28 AND month = 7;

-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.

-- Read the interviews from people in the crime scene
.schema interviews
SELECT * FROM interviews WHERE day = 28 AND month = 7 AND transcript LIKE "%bakery%";

-- Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
-- If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.

-- I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery,
-- I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

-- As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were
-- planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.

-- Read who withdraw money from the atm before the crime
.schema atm_transactions
SELECT * FROM atm_transactions WHERE day = 28 AND month = 7 AND year = 2021 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';

-- Read who got in and out of the bakery between 10:15 and 10:25 of the day of the crime
.schema bakery_security_logs
SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25;

-- Read travels
.schema flights
.schema airports
.schema passengers
-- Read earliest flight one day after the crime(29)
SELECT * FROM flights WHERE origin_airport_id = 8 AND year = 2021 AND month = 7 AND day = 29 ORDER BY hour ASC;

-- Read passengers from that flight, with some extra information from the people table
SELECT people.passport_number, people.name, people.phone_number, people.license_plate
FROM passengers
JOIN people ON people.passport_number = passengers.passport_number
WHERE flight_id = 36;

-- Read calls that happened in the day of the crime with a duration of one minute or less
SELECT caller, receiver
FROM phone_calls
WHERE year = 2021 AND
month = 7 AND
day = 28 AND
duration <= 60;

-- Read rows from the people that received a call or called on the day of the robbery and are on the plane on the earliest flight from the next day
SELECT *
FROM people
WHERE
    phone_number IN (
        SELECT caller
        FROM phone_calls
        WHERE year = 2021 AND
        month = 7 AND
        day = 28 AND
        duration <= 60
    )
    OR phone_number IN (
        SELECT receiver
        FROM phone_calls
        WHERE year = 2021 AND
        month = 7 AND
        day = 28 AND
        duration <= 60
    )
    AND passport_number IN (
        SELECT passport_number
        FROM passengers
        WHERE flight_id = 36
    )
;

-- Read rows from the people that called on the day of the robbery and are on the plane on the earliest flight
-- from the next day and withdraw money before the robbery and were in the bakery
SELECT *
FROM people
WHERE
    phone_number IN (
        SELECT caller
        FROM phone_calls
        WHERE year = 2021 AND
        month = 7 AND
        day = 28 AND
        duration <= 60
    )
    AND passport_number IN (
        SELECT passport_number
        FROM passengers
        WHERE flight_id = 36
    )
    AND id IN (
        SELECT person_id
        FROM bank_accounts
        WHERE account_number IN (
            SELECT account_number
            FROM atm_transactions
            WHERE day = 28 AND
            month = 7 AND
            year = 2021 AND
            atm_location = 'Leggett Street' AND
            transaction_type = 'withdraw'
        )
    )
    AND license_plate IN (
        SELECT license_plate
        FROM bakery_security_logs
        WHERE year = 2021 AND
        month = 7 AND
        day = 28 AND
        hour = 10 AND
        minute BETWEEN 15 AND 25
    )
;
-- Bruce

-- Who Bruce called
SELECT *
FROM people
WHERE phone_number = (
    SELECT receiver
    FROM phone_calls
    WHERE caller = (
        SELECT phone_number
        FROM people
        WHERE name = 'Bruce'
    )
    AND year = 2021
    AND month = 7
    AND day = 28
    AND duration <= 60
)
;


