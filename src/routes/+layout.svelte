<script>
	import Selector from '$lib/SELECTOR.svelte'
	import _ from "lodash"
	import NavigationVertical from "$lib/NavigationVertical.svelte"
	import { browser } from "$app/environment"
	import { site } from '$lib/site.js'
	import { query,innerwidth,multiselect } from '$lib/query.js'
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

<!-- <label>
	<input type=range bind:value={WIDTH} min=150 max=1000>
</label> -->

<label>
	<input type=range bind:value={$innerwidth} min=250 max=1600 style="width:500px">
</label>

{$innerwidth}


<div class="menu">
	<img class="logo" src="/images/WASA_SK_LOGO_v2.png" title="Wasa SK" alt="" on:click={()=> goto("/query")} on:keydown={noop}>

	<Selector label='ålder' chars=1 bind:result={$multiselect[0]} values={'Knatte Minior Junior Senior Veteran'} />
	<Selector label='typ'   chars=1 bind:result={$multiselect[1]} values={'Meddelande Inbjudan Träning Program Resultat Game Diverse'} />
	<Selector label='lag'   chars=1 bind:result={$multiselect[2]} values={'Individ Lag'} />
	<Selector label='nivå'  chars=1 bind:result={$multiselect[3]} values={'KM DM SM NM EM WM'} />
	<Selector label='tid'   chars=1 bind:result={$multiselect[4]} values={'Blixt Snabb Halv Lång'} />
	<Selector label='kön'   chars=1 bind:result={$multiselect[5]} values={'Kvinna Man'} />
	<Selector label='år'    chars=4 bind:result={$multiselect[6]} values={'2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024'} />

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
