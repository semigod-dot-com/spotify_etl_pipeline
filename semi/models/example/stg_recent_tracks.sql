WITH raw as (
    select * FROM spotify_dbt.recent_tracks
),
stg_recent_tracks as (
    select
        CAST("played_at" AS TIMESTAMP) as Played_At,
        "track_name" AS Track_Name,
        "artist_name" AS Artist_Name,
        "album" as Album,
        CAST("release_date" AS TIMESTAMP) AS Release_Date,
        CAST("duration_ms" AS INT) AS Duration_MS,
        "track_id" AS Track_Id,
        "track_uri" AS Track_Uri
    from raw
)

SELECT * FROM stg_recent_tracks