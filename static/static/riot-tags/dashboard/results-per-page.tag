<results-select>
	<style type="text/css"> 



	</style>
	
  
	<label>Results</label> <br>
	<select  onchange={ updateResults } name='resultSelect'>
  	<option id="option{ result }" each={ result in opts.results }>{ result }</option>
	</select>
 

  


<script>
q = riot.route.query()
page = q.page
results = q.results

var self = this

this.on('mount',function(){
	tag = `#option${results}`
	$(tag).prop('selected',true)
})

updateResults(e){
	results = this.resultSelect.value
  url = `transactions/${opts.slug}/?page=${page}&results=${results}`
  this.linkTo(url)
}


linkTo(url){
  riot.route(url)
}




</script>

</results-select>