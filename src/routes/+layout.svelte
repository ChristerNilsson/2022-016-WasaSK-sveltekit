<script>
	import _ from "lodash"
	import Selector from '$lib/components/SELECTOR.svelte'
	import NavigationVertical from "$lib/components/NavigationVertical.svelte"
	import { browser } from "$app/environment"
	import { log } from '$lib/utils.js'
	import { site,dimensions,query,innerwidth,a,b,c,d,e,f,g,h } from '$lib/stores.js'
	import { goto } from '$app/navigation'
	import './styles.css'

	export const prerender = true

	let WIDTH = 400
	let INNERWIDTH = 750
	const COLUMNS = 1

	let innerWidth = 0
	let innerHeight = 0

	const GAP = 1

	let stack = ["Hem"]
	let path = [$site.menu]

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
				log('A',url)
				window.open(url)
			} else if (_.startsWith(url,'/')) {
				log('B',url)
				goto(url)
			} else if (_.endsWith(url,'.md')) {
				log('C',url)
				goto('/post/' + url)
			} else if (_.endsWith(url,'.html')) {
				log('D',url)
				goto('/post/' + url)
			} else if (_.startsWith(url,'files')) { 
				log('E',url)
				window.open('../src/lib/' + url)
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

	function home() {
		query.set("")
		goto("/query")
	}

</script>

<svelte:window bind:innerWidth bind:innerHeight />

<label><input type=range bind:value={$innerwidth} min=250 max=1600 style="width:500px"></label>

{$innerwidth}

<div class="menu">
	<img class="logo" src="/images/WASA_SK_LOGO_v2.png" title="Wasa SK" alt="" on:click={home} on:keydown={noop}>
	<!-- '_ Junior Senior' -->
	<Selector label='ålder'   chars=1 bind:result={$a} values={$dimensions.ålder} />
	<Selector label='typ'     chars=1 bind:result={$b} values={$dimensions.typ} />
	<Selector label='lag'     chars=1 bind:result={$c} values={$dimensions.lag} />
	<Selector label='nivå'    chars=1 bind:result={$d} values={$dimensions.nivå} />
	<Selector label='tid'     chars=1 bind:result={$e} values={$dimensions.tid} />
	<Selector label='kön'     chars=1 bind:result={$f} values={$dimensions.kön} />
	<Selector label='år'      chars=4 bind:result={$g} values={$dimensions.år} />
	<Selector label='posttyp' chars=1 bind:result={$h} values={$dimensions.posttyp} />

	<NavigationVertical {keys} {push} {WIDTH} />
</div>

<div class="swimlane" style="left:405px; width:{$innerwidth}px">
	<slot />
</div>

<style>

	/* input { width:500px } */

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
