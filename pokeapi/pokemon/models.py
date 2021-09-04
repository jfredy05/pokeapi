from django.db import models


class PokeModel(models.Model):
	"""
	Acts as an abstract base class
	"""
	modified = models.DateTimeField('Modified at', auto_now=True)
	created = models.DateTimeField('Created at', auto_now_add=True)

	class Meta:
		abstract = True


class EvolutionChain(PokeModel):
	"""
	Evolution Chain Model
	"""
	id_chain = models.PositiveIntegerField('Id Chain', unique=True)

	class Meta:
		verbose_name = "Evolution Chain"
		verbose_name_plural = "Evolution Chains"
		ordering = ['id_chain']


class Pokemon(PokeModel):
	"""
	Pokemon Info Model
	"""
	chain = models.ForeignKey(EvolutionChain, on_delete=models.CASCADE)
	id_pokemon = models.PositiveIntegerField('Id Pokemon', unique=True)
	name = models.CharField("Name", max_length=100)
	image = models.CharField('Image', max_length=150, blank=True, null=True)
	height = models.PositiveIntegerField('Height')
	weight = models.PositiveIntegerField('Weight')
	order = models.PositiveIntegerField('Order')

	class Meta:
		verbose_name = "Pokémon"
		verbose_name_plural = "Pokémon"

	def __str__(self):
		return self.name


class Stats(PokeModel):
	"""
	Base stats Pokémon
	"""
	pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
	name = models.CharField("Name", max_length=100)
	base = models.PositiveIntegerField('Base stat')
	effort = models.PositiveIntegerField('effort')

	class Meta:
		verbose_name = "Base Stat"
		verbose_name_plural = "Base Stats"

	def __str__(self):
		return self.name
