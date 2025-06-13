{{ config(
    materialized='incremental',
    unique_key='played_at'
) }}

WITH raw AS (
    SELECT * FROM spotify_dbt.recent_tracks
),

stg_recent_tracks AS (
    SELECT
        CAST("played_at" AS TIMESTAMP) AS Played_At,
        "track_name" AS Track_Name,
        "artist_name" AS Artist_Name,
        "album" AS Album,
        CAST("release_date" AS TIMESTAMP) AS Release_Date,
        CAST("duration_ms" AS INT) AS Duration_MS,
        "track_id" AS Track_Id,
        "track_uri" AS Track_Uri
    FROM raw

    {% if is_incremental() %}
        WHERE CAST("played_at" AS TIMESTAMP) > (SELECT MAX(played_at) FROM {{ this }})
    {% endif %}
),

with_row_number AS (
    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY artist_name ORDER BY played_at DESC
        ) AS row_num
    FROM stg_recent_tracks
)

SELECT * FROM with_row_number
