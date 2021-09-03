# devprofile-api

This is the backend service for a mobile application that enables recruiters to easily find and hire software developers 


## Technologies 

The following technologies were used in this project:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [AWS S3 Bucket](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Categories=categories%23storage&trk=ps_a134p000006pahTAAQ&trkCampaign=acq_paid_search_brand&sc_channel=PS&sc_campaign=acquisition_EEM&sc_publisher=Google&sc_category=Storage&sc_country=EEM&sc_geo=EMEA&sc_outcome=acq&sc_detail=aws%20s3&sc_content=S3_e&sc_matchtype=e&sc_segment=495021970248&sc_medium=ACQ-P%7CPS-GO%7CBrand%7CDesktop%7CSU%7CStorage%7CS3%7CEEM%7CEN%7CText%7Cxx%7CNon-EU&s_kwcid=AL!4422!3!495021970248!e!!g!!aws%20s3&ef_id=CjwKCAjwybyJBhBwEiwAvz4G7yqCcl_Ejk1QgG6y4hpcLjcQszuvM5KI2OBhgxJyjyonljImRHCrLBoC0dkQAvD_BwE:G:s&s_kwcid=AL!4422!3!495021970248!e!!g!!aws%20s3&awsf.Free%20Tier%20Types=*all)


## Requirements

Before starting, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/) installed.

Kindly ensure that you are in the root directory before running the following commands.

## Create a virtual environment

    python3 -m venv env

## Activate the virtual environment

    . env/bin/activate

## Install dependencies

    pip install -r requirements.txt

## Navigate to the source directory

    cd src

## Make migrations

    python manage.py makemigrations

## Migrate apps and database

    python manage.py migrate

## Run Tests

    python manage.py test

## Start server

    python manage.py runserver


# API Expected Response

## success response

    {
        "message": "success",
        "data": {
            "<string>: <string>,
            <string>: <string>,
            <string>: <string>
        },
        "errors": null
    }

# error response

    {
        "message": "failure",
        "data": null,
        "errors": {
            "message": <string>
        }
    }
