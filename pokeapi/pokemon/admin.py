from django.contrib import admin

from .models import EvolutionChain, Pokemon, Stats


class EvolutionChainAdmin(admin.ModelAdmin):
	list_display = ('id', 'id_chain', 'modified', 'created')


admin.site.register(EvolutionChain, EvolutionChainAdmin)


class StatsAdmin(admin.StackedInline):
	model = Stats
	extra = 1


class PokemonAdmin(admin.ModelAdmin):
	list_display = ('name', 'id_pokemon', 'modified', 'created', 'order')
	list_filter = ('chain', )
	inlines = (StatsAdmin,)


admin.site.register(Pokemon, PokemonAdmin)
