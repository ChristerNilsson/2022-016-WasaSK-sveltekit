import { readable } from 'svelte/store'
import data from './site.json'

function stop () {}
function start (set) {return stop}
function selected(a,b) {return a+b}

export const site = readable(data, start)

console.log('store:site loaded')