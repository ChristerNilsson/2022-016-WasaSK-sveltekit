import { readable } from 'svelte/store'
import data from './site.json'
function stop () {}
function start (set) {return stop}
export const site = readable(data, start)
console.log('store:site loaded')