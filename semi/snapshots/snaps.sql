{% snapshot snap_stg_recent_tracks %}
{{
    config(
        target_schema='spotify_dbt',
        unique_key='played_at',
        strategy='timestamp',
        updated_at='played_at'
    )
}}

SELECT * FROM {{ ref('stg_recent_tracks') }}

{% endsnapshot %}
