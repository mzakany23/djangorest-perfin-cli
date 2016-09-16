<pagination-list>
	<p>page { opts.pag.current_page } of { opts.pag.max_pages } total pages</p> <br>
	<p>{ currentAccount } has { opts.pag.total_records } transactions counted</p>
<nav>
  <ul class="pagination">
    <li>
      <a onclick={ prev } href="" aria-label="Previous">
        <span aria-hidden="true">&laquo;</span>
      </a>
    </li>

    <li class="{ active: currentPage === pageNum }" each={ pageNum in pages }><a onclick={ getPageNum } href="#">{ pageNum }</a></li>
    
    <li>
      <a onclick={ next } href="#" aria-label="Next">
        <span aria-hidden="true">&raquo;</span>
      </a>
    </li>
  </ul>
</nav>

<script>
		    	

	this.on('mount',function(){
		this.currentPage = parseInt(opts.pag.current_page)
		this.pages = []
		for (var i = 1; i<= parseInt(opts.pag.max_pages);i++ ){
			this.pages.push(i)
		}
		this.update()
	})

	 // pagination buttons
    hasNextPage(){
        return opts.pag.has_next === 'True'
    }

    next(){
        nextPage = this.currentPage+1
        if (this.hasNextPage()) this.linkTo(nextPage);
    }

    prev(){
        prevPage = this.currentPage - 1
        if (prevPage >= 1) this.linkTo(prevPage)
    }

    getPageNum(e){
        pageNum = e.item.pageNum
        this.linkTo(pageNum)
    }

    linkTo(pageNum){
        q = riot.route.query()
        if (q.results){
          riot.route(`/transactions/${opts.account}/?page=${pageNum}&results=${q.results}`)    
        }
        
        scroll(0,0)
    }

    setMaxPageCount(num){
        for (var i=1; i<=num;i++){
            this.maxPageCount.push(i)
        }
    }
</script>

</pagination-list>