from tastypie.resources import ModelResource
from tastypie import fields
from models import *
from tastypie.resources import ALL_WITH_RELATIONS
from pprint import pprint


class PersonResource(ModelResource):

    class Meta:
        queryset = Person.objects.all()


class CheckpointResource(ModelResource):
    class Meta:
        queryset = Checkpoint.objects.all()

class RaceResource(ModelResource):

    runners = fields.OneToManyField('iRFmap.api.RunnerResource', 'runners', full=True)
    checkpoints = fields.OneToManyField('iRFmap.api.CheckpointResource', 'checkpoints', full=True, null=True)

    class Meta:
        queryset = Race.objects.all()

        filtering = {
            'runners': ALL_WITH_RELATIONS,
            'checkpoints': ALL_WITH_RELATIONS
        }

    def dehydrate(self, bundle):
        '''
        Add custom fields here to avoid complex processing in JS
        '''


class RunnerResource(ModelResource):
    """
    Query for a race by ID and get back a list of runners (as people)
    """

    person = fields.ForeignKey(PersonResource, 'person', full=True)
    race = fields.ForeignKey(RaceResource, 'race')

    class Meta:
        queryset = Runner.objects.all()
        excludes = ['race']

        filtering = {
            'race': ALL_WITH_RELATIONS
        }

