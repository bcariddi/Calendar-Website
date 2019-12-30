# API Documentation

## Events 
* `events`

### Get All Events
* `/all`
* Returns a JSON array of all events

#### GET Parameters
* `sortBy`
	* default: startDate
	* sorts array
* `count`
	* number of events to return
	
### Create Event
* `/new/<organizationID>`
* Creates an event for a specific organization from a form using POST

### Update Event
* `/update/<id>`
* Updates the chosen event from a form using POST 

## Delete Event
* `/update/<id>`
* Deletes the event with the provided id

## User Management (For Admins)
* `/account/manage`

### Create User
* `/create`

### Delete User
* `/delete/<id>`

## Current User
* `/account`

### Logging In and Out
* `/login`
* `/logout`

### Saving an Event
* `/save`
* `/unsave`

#### GET Parameters
* `id`
	* Event id 
	
### Following a Club
* `/follow`
* `/unfollow`

#### GET Parameters
* `id`
	* Organization id 
	
## Other Users
* `/user`

### Find User
* `/<username>`
	* returns a JSON object of the requested user
	
## Organizations
* `/orgs`

### All Organizations
*  `all/`

### Create Organizations
*  `create/`

### Organization
*  `<id>/`


