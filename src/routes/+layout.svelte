<script>
	import _ from "lodash"
	import Selector from '$lib/components/SELECTOR.svelte'
	import NavigationVertical from "$lib/components/NavigationVertical.svelte"
	import { browser } from "$app/environment"
	import { site,query,innerwidth,a,b,c,d,e,f,g } from '$lib/stores.js'
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
				window.open(url)
			} else if (_.startsWith(url,'/')) {
				goto(url)
			} else if (_.endsWith(url,'.md')) {
				goto('/post/' + url)
			} else if (_.endsWith(url,'.html')) {
				goto('/post/' + url)
			} else if (_.startsWith(url,'files')) { 
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

</script>

<svelte:window bind:innerWidth bind:innerHeight />

<label><input type=range bind:value={$innerwidth} min=250 max=1600 style="width:500px"></label>

{$innerwidth}

<div class="menu">
	<img class="logo" src="/images/WASA_SK_LOGO_v2.png" title="Wasa SK" alt="" on:click={()=> goto("/query")} on:keydown={noop}>

	<Selector label='ålder' chars=1 bind:result={$a} values={'_ Junior Senior'} />
	<Selector label='typ'   chars=1 bind:result={$b} values={'_ Resultat Notis Inbjudan Träning Program Game Diverse'} />
	<Selector label='lag'   chars=1 bind:result={$c} values={'_ Individ Lag'} />
	<Selector label='nivå'  chars=1 bind:result={$d} values={'_ KM DM SM NM EM WM'} />
	<Selector label='tid'   chars=1 bind:result={$e} values={'_ Blixt Snabb Lång'} />
	<Selector label='kön'   chars=1 bind:result={$f} values={'_ Kvinna Man'} />
	<Selector label='år'    chars=4 bind:result={$g} values={'____ 2023 2022 2021 2020 2019 2018 2017 2016 2015 2014 2013 2012 2011 2010'} />

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
