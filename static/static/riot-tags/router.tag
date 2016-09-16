<router>
	
<script>
	self = this
	var currentTag = null
	var currentRoute = null
	var path = window.location.pathname;
	var lastRoute = null
	var lastFullRoute = null
	var url = 'http://localhost:8001/riot'
	var mainUrl = 'http://localhost:8001/api'

	function mount(tag,options){
		currentTag && currentTag.unmount(true)
		currentTag = riot.mount('div#tags',tag,options)[0]
	}

	var routes = {
		account: function(id,action){
			q = riot.route.query()
			pageNum = q.page 
			results = q.results
			
			if (pageNum && results){
			
			}else if (pageNum){
			
			}else{
				// $.get('http://localhost:8001/api/transactions').then((transactions) => {
				// 	mount('transaction-list',{bus:bus,transactions:transactions})
				// }).fail((e) => {console.log(e)})
				
			}
		},
		transactions: function(account,action){
			q = riot.route.query()
			pageNum = q.page 
			results = q.results
			
			if (account && pageNum && results){
				$.get(`${url}/transactions/${account}/?page=${pageNum}&results=${results}`).then((model) => {
					currentAccount = model.results[0].account.title
					mount('transaction-list',{bus:bus,model:model,currentAccount:currentAccount,slug:account})
				})
			}else if (pageNum){
				route = `/transactions/fifth-third/?page=1&results=20`
				riot.route(route)
			}else{

				 // console.log(`${mainUrl}/transactions/${account}/?from=${q.from}&to=${q.to}`)

				 $.get(`${mainUrl}/transactions/${account}/?from=${q.from}&to=${q.to}`).then((transactions) => {
					try{
						currentAccount = transactions[0].account.title	
					}catch(e){
						currentAccount = 'None'
					}
					
					model = {
						results: transactions
					}
					month = q.from.slice(0,2)
					monthConverter = {
						'01': 'January',
						'02': 'February',
						'03': 'March',
						'04': 'April',
						'05': 'May',
						'06': 'June',
						'07': 'July',
						'08': 'August',
						'09': 'September',
						'10': 'October',
						'11': 'November',
						'12': 'December',
					}
					year = q.from.substr(q.from.length - 4)
				 	mount('transaction-list',{
				 		bus:bus,model:model,
				 		currentAccount:currentAccount,
				 		slug:account,
				 		month:monthConverter[month],
				 		year:year,
				 	})
				 	
				 }).fail((e) => {console.log(e)})
			}
		}
	}

	function redirectTo(url){
		window.location.replace(url)
	}

	function handler(collection,id,action){
		lastRoute = collection
		lastFullRoute = `${path}#${collection}`
		// lastRoute = collection
	
		var fn = routes[collection || 'home']
		if (fn) {
			fn(id,action)
		}else{
			riot.route('/transactions/?page=1')
		}
	}
	
	riot.route(handler);
</script>

</router>