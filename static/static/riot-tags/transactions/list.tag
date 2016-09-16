<transaction-list>
    <style type="text/css">
        .list{
            margin-top: 30px;
        }

        tr.hover:hover{
            background-color: red;
        }

        #date{}

        .scrolling{
            max-height: 250px;
            top: 0;
            position: relative;
            overflow: scroll;

        }

        .filter-bar{
            background-color: grey;
        }
    </style>

<pagination-list pag={ opts.model.pagination } account={ opts.slug }></pagination-list>

<div class="row">
    <h1>Search</h1>
    <div class="col-md-2">
        <filter-list bus={ opts.bus } records={ opts.model.results }></filter-list>
    </div>
</div>

<div class="row">
    <h2>Search all Transactions</h2>
    <div class="col-md-1">
        <results-select results={ [10, 20,50,100] } slug={ opts.slug }></results-select>
    </div>

    <div class="col-md-2">
    <label>Accounts</label> <br>
        <select onchange={ changeAccount } name='accountSelect'>
            <option id='fifth-third' value="fifth-third">Fifth Third</option>
            <option id='chase-united' value='chase-united'>Chase United</option>
        </select>
    </div>

</div>

<div class="row">
<h2>Search by Month</h2>
<div class="col-md-1">
        <label>Month</label> <br>
        <select onchange={ searchByMonth } name='monthsSelect'>
            <option>None</option>
            <option>January</option>
            <option>February</option>
            <option>March</option>
            <option>April</option>
            <option>May</option>
            <option>June</option>
            <option>July</option>
            <option>August</option>
            <option>September</option>
            <option>October</option>
            <option>November</option>
            <option>December</option>

        </select>
    </div>

    <div class="col-md-2">
        <label>Years</label> <br>
        <select onchange={ updateYear } name='yearsSelect'>
            <option>2015</option>
            <option>2016</option>
        </select>
    </div>
</div>
	<div class="row">
		<div class="col-md-8">
        
        

        <div class="panel panel-primary filterable list">
            <div class="panel-heading">
                <h3 class="panel-title">{ opts.currentAccount } Transactions</h3>
            </div>
            <table class="table">
                
            
            <th><a onclick={ sortByDate } href="">Date</a></th>
            <th><a onclick={ sortByDescription } href="">Description</a></th>
            <th><a onclick={ sortByAmount } href="">Amount</a></th>

                <tbody>
                    <tr each={ transaction,i in opts.model.results } class="{ danger: transaction.amount < -1000 } hover">
                       
                        <td id='date'>{ transaction.date }</td>
                        <td><a onclick={ sumByTransaction } href="">{ transaction.name }</a></td>
                        <td>${ transaction.amount }</td>
                        
                    </tr>
                    
                </tbody>
            </table>
        </div>
        
    </div>

    <div class="col-md-4">
       <div if={ totals } class="panel panel-primary filterable list"> 
        <div class="panel-heading"> 
            <h3 class="panel-title">{ opts.currentAccount } Totals</h3> 
        </div> 
        <table class="table"> 
            <tbody>
                <tr>
                    <th>Date</th>
                    <th>Description</th> 
                    <th>Amount</th> 
                </tr>
            </tbody>

            <tbody> 

                <tr each={ transaction in totals.store }> 
                    <td>{ transaction.date }</td>
                    <td >{ transaction.name }</td>
                    <td>${ transaction.amount }</td> 
                </tr>

                <tr>
                    <td>Total: ${ parseFloat(totals.total).toFixed(2) }</td>
                    <td>Count: { totals.count }</td>
                </tr>
            </tbody> 
        </table> 
        </div>
    </div>
  </div>

<script>
    self = this
    q = riot.route.query()
    page = q.page
    results = q.results 
    this.selectedYear = 2015
    this.selectedAccount = 'fifth-third'
    
    // mount
    this.on('mount',function(){
        tag = `#${opts.slug}`
        $(tag).prop('selected',true)
        this.monthsSelect.value = opts.month
        this.yearsSelect.value = opts.year
    })

    // actions
    sortByDescription(){
        opts.model.results = _.sortBy(opts.model.results,'name')    
        this.update()
    } 

    updateYear(){
        this.selectedYear = parseInt(this.yearsSelect.value)
        console.log(q.from)
        url = `/transactions/${this.accountSelect.value}/?from=${q.from.slice(0,2)}/01/${this.selectedYear}&to=${q.to.slice(0,2)}/31/${this.selectedYear}`
        riot.route(url)
    }



    searchByMonth(){
        month = this.monthsSelect.value

        switch (month) {
            case 'January':
                url = `/transactions/${this.accountSelect.value}/?from=01/01/${opts.year}&to=01/31/${opts.year}`
                break
            case 'February':
                url = `/transactions/${this.accountSelect.value}/?from=02/01/${opts.year}&to=02/28/${opts.year}`
                
                break
            case 'March':
                url = `/transactions/${this.accountSelect.value}/?from=03/31/${opts.year}&to=03/31/${opts.year}`
                
                break
            case 'April':
                url = `/transactions/${this.accountSelect.value}/?from=04/01/${opts.year}&to=04/30/${opts.year}`
                
                break
            case 'May':
                url = `/transactions/${this.accountSelect.value}/?from=05/01/${opts.year}&to=05/31/${opts.year}`
                
                break
            case 'June':
                url = `/transactions/${this.accountSelect.value}/?from=06/01/${opts.year}&to=06/30/${opts.year}`
                
                break
            case 'July':
                url = `/transactions/${this.accountSelect.value}/?from=07/01/${opts.year}&to=07/31/${opts.year}`
                
                break
            case 'August':
                url = `/transactions/${this.accountSelect.value}/?from=08/01/${opts.year}&to=08/31/${opts.year}`
                
                break
            case 'September':
                url = `/transactions/${this.accountSelect.value}/?from=09/01/${opts.year}&to=09/30/${opts.year}`
                
                break
            case 'October':
                url = `/transactions/${this.accountSelect.value}/?from=10/01/${opts.year}&to=10/31/${opts.year}`
                
                break
            case 'November':
                url = `/transactions/${this.accountSelect.value}/?from=11/01/${opts.year}&to=11/30/${opts.year}`
                
                break
            case 'December':
                url = `/transactions/${this.accountSelect.value}/?from=12/01/${opts.year}&to=12/31/${opts.year}`
                break
        }

      riot.route(url)

    }  


    sortByAmount(){
        opts.model.results = _.sortBy(opts.model.results,'amount').reverse()
        this.update()
    }

    sortByDate(){
        opts.model.results = _.sortBy(opts.model.results,'date')
        this.update()
    }


    sumByTransaction(e){
        e.preventDefault()
        trans = e.item.transaction
        results = {
            total:0,
            count: 0,
            store: []
        }

        for (var key in opts.model.results){
            found = opts.model.results[key]
            foundKey = found.name.replace(/\s+/g,'').replace(/\*+/g,'').slice(0,10)
            transKey = trans.name.replace(/\s+/g,'').replace(/\*+/g,'').slice(0,10)
            if (foundKey === transKey){
                results.store.push(found)
                results.count += 1
                amt = parseFloat(found.amount)
                results.total += amt
            }
        }
        this.totals = results

    }

    changeAccount(){
        account = this.accountSelect.value
        riot.route(`transactions/${account}/?page=1&results=10`)
    }

    this.opts.bus.on('results',function(results){
        self.totals = results
        self.update()
    })

</script>

</transaction-list>
