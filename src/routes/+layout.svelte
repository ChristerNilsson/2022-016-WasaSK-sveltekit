<script>
	import _ from "lodash"
	import NavigationVertical from "../lib/NavigationVertical.svelte"
	import NavigationHorisontal from "../lib/NavigationHorisontal.svelte"
	import Search from "../lib/Search.svelte"
	import site from "../lib/site.json"
	import { goto } from '$app/navigation'
	import './styles.css'

	let sokruta = ""
	let selected = {} // filenames

	const COLUMNS = 1

	$: WIDTH = 250
	const GAP = 1

	let stack = ["Hem"]
	let path = [site.menu]

	const round = (x,n) => Math.round(x*Math.pow(10,n))/Math.pow(10,n)
	const spreadWidth = (share,WIDTH) => Math.floor((WIDTH-2*GAP*(1/share+1))*share) - 2

	$: keys = _.keys(_.last(path))

	function push(key) {
		const obj = _.isObject(_.last(path)[key])
		if (obj) {
			path.push(_.last(path)[key])
			stack.push(key)
			path = path
			stack = stack
		} else {
			const url = _.last(path)[key]
			if (_.startsWith(url,'http')) {
				window.open(url,"_self")
			} else if (_.startsWith(url,'/')) {
				goto(url)
			} else if (_.isNumber(url)) {
				goto('/post/' + url)
			} else { // .pdf etc
				window.open('../src/lib/files/' + url,"_self")
			}
		}
	}

	function pop() {
		path.pop()
		stack.pop()
		path = path
		stack = stack
	}

	function noop() {}

	const innerWidth = 1920

	$: w = [innerWidth-WIDTH-10,(innerWidth-WIDTH-20)/2,(innerWidth-WIDTH-30)/3]
	$: p = (COLUMNS==1) ?  [WIDTH] :
				 ((COLUMNS==2) ? [WIDTH,WIDTH+w[1]+10] :
												 [WIDTH,WIDTH+w[2]+10,WIDTH+w[2]+w[2]+20])
	
</script>

<div class="menu">
	<img class="logo" src="../src/lib/images/WASA_SK_LOGO_v2.png" title="Wasa SK" alt="" on:click={()=> goto("/post")} on:keydown={noop}>
	<Search bind:sokruta  {stack} {WIDTH} {GAP} {spreadWidth} {_} {pop} />
	<NavigationHorisontal {stack} {WIDTH} />
	<NavigationVertical {keys} {push} {WIDTH} />
</div>

<div class="swimlane" style={"left:260px; width:"+w[0]+"px"}>
	<slot />
</div>

<style>
	.logo {
		width:100px;
		height:auto;
		padding-left:10px;
		padding-top:10px;
		padding-bottom:10px;
	}
	.swimlane {
			position: absolute;
			top: 0px;
	}
</style>
