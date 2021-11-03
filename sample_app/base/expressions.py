from django.db.models import Subquery
from django.db.models.expressions import Value
from django.db.models.fields import IntegerField


class SubqueryAgg(Subquery):
    def __init__(self, queryset, expression, *args, distinct=False, **kwargs):
        queryset = queryset \
            .annotate(_subquery_agg_group=Value(1, output_field=IntegerField())) \
            .values('_subquery_agg_group') \
            .annotate(_subquery_agg_result=expression) \
            .values('_subquery_agg_result')

        super().__init__(queryset, *args, **kwargs)
