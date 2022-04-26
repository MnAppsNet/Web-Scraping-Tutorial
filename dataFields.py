#=====================================================================#
# This is the structure of the collected data from TripAdvisorScraper #
#=====================================================================#
class field:
    ID = "_id"
    class id:
        ID = 'id'
        POI_LOCATION_ID = 'poi_location_id'
        GEOLOCATION = 'geolocation'

    POI_NAME = 'poi_name'
    TITLE = 'title'
    DATE = 'date'
    REVIEW_RATING = 'review_rating'
    TEXT = 'text'
    DATE_OF_VISIT = 'date_of_visit'

    REVIEWER = 'reviewer'
    class reviewer:
        NAME = 'name'
        HANDLE = 'handle'
        LOCATION = 'location'
        AGE = 'age'
        SEX = 'sex'
        CONTRIBUTIONS = 'contributions'
        HELPFUL_VOTES = 'helpful_votes'
        CITIES_VISITED = 'cities_visited'
        PHOTO = 'photo'

        DISTRIBUTION = 'distribution'
        class distribution:
            EXCELLENT = 'Excellent'
            VERY_GOOD = 'Very Good'
            AVERAGE = 'Average'
            POOR = 'Poor'
            TERRIBLE = 'Terrible'