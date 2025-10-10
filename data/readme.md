# DATA DESCRIPTION

The directory includes different files used as data inputs for the analysis presented. These files include:

* *data_set_raw_100.csv*: Includes a sample of the validations used to build the complex networks.
* *kind_of_tickets_segmentation_or.csv*: is the list of the different types of tickets available from the ACTV. For simplification reasons, they have being grouped on 'tourist' or 'resident' categories.
* *stop_aggr.json*: is the file describing how stops that are considered different in the raw validations dataset can be grouped in a logical manner. It means if a stop has two boarding docks, they appear as different places of validation in the dataset, but they can be considered the same stop.
* *stops.csv*: it contains the information of each of the stops, including an ID and a geographic location (lat,lon), used for visualization pourposes.

The contents of each file are as folows:

## data_set_raw_100

* id: Unique identifier for each record (row).
* data_validazione: Date and time of ticket validation (when the passenger boarded).
* seriale: Ticket serial number or unique identifier for the traveler's ticket.
* fermata: Numeric code for the stop where validation occurred.
* descrizione: Name or description of the stop.
* titolo: Code for the type of ticket used.
* descrizione_titolo: Description of the ticket type (duration, price, etc.).
* lon: Longitude of the stop.
* lat: Latitude of the stop.

## kind_of_tickets_segmentation_or

* descrizione_titolo: Description or name of the ticket type.
* titolo: Code or identifier for the ticket type.
* avg_stops: Average number of stops traveled per ticket.
* num_tickets: Total number of tickets of this type issued.
* type: Category of the ticket holder (e.g., Tourist, Worker, Student, Retired, Other).
* period: Validity period or duration of the ticket (e.g., 1 day, 3 days, 1 Year, 75 mins).

## stops

* stop_id: Unique identifier for each stop (row).
* fermata: Numeric code for the stop, used in ticket validation and network construction.
* descrizione: Name or description of the stop.
* lat: Latitude coordinate of the stop.
* lon: Longitude coordinate of the stop.

## stop_aggr

* Key: The original stop code from the dataset.
* Value: The grouped stop code to which it should be aggregated. If multiple physical stops (e.g., different boarding docks) are considered the same logical stop, they are mapped to a single code. Codes mapped to -1, -2, etc., likely represent stops that are excluded, undefined, or grouped in a special way.  

This mapping is used to consolidate stop data for network construction and analysis.
