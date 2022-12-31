import { readable } from 'svelte/store'
import { writable } from 'svelte/store'
import data from '$lib/data/site.json'
import dims from '$lib/data/dimensions.json'

function stop () {}
function start (set) {return stop}

export const site = readable(data, start)
export const dimensions = readable(dims, start)

export const query = writable("", start)
export const innerwidth = writable(1000, start)
export const a = writable('nix',start) // ålder
export const b = writable('nix',start) // typ
export const c = writable('nix',start) // lag
export const d = writable('nix',start) // nivå
export const e = writable('nix',start) // tid
export const f = writable('nix',start) // kön
export const g = writable('nix',start) // år
export const h = writable('nix',start) // filer
