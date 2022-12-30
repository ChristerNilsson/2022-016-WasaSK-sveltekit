import { writable } from 'svelte/store'

function stop () {}
function start (set) {return stop}

export const query = writable("", start)
export const innerwidth = writable(1000, start)

export const a = writable('nix',start)
export const b = writable('nix',start)
export const c = writable('nix',start)
export const d = writable('nix',start)
export const e = writable('nix',start)
export const f = writable('nix',start)
export const g = writable('nix',start)

console.log('store:writable loaded')