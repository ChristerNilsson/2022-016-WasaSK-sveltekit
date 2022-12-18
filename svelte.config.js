import adapter from '@sveltejs/adapter-auto';
import { mdsvex } from 'mdsvex';
import preprocess from 'svelte-preprocess';
import sveltePreprocess from 'svelte-preprocess'

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter()
	},
	extensions: ['.svelte', '.md'],
  preprocess: [
		sveltePreprocess(),
    preprocess(),
    mdsvex({
      extensions: ['.md']
    })
  ]	
};

export default config;
