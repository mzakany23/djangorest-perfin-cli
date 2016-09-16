<filter-list>
	<style type="text/css">
		label{
			margin-right: 5px;
		}
	</style>

	<form onsubmit={ search }>
	<label>Filter list by word</label> <br>
	<input type='text' placeholder='web initiated' name="textSearch">
	<button>Filter</button>
	</form>
<script>
var self = this

var results = {
    total:0,
    count: 0,
    store: []
}

	search(e){
		results.total = 0
		results.count = 0 
		results.store = []

		_.filter(opts.records,this.findByName)
		opts.bus.trigger('results',results)
	}

	findByName(obj){
		search = this.textSearch.value.toLowerCase()
		nameArr = obj.name.split(' ')
		for (var key in nameArr){
			word = nameArr[key].toLowerCase()
			if (word === search){
				results.store.push(obj)
				amt = parseFloat(obj.amount)
				results.total += amt 
				results.count += 1
			}
		}
	}
</script>

</filter-list>