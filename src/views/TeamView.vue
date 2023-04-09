<template>
    <div>
        <input type="text" v-model="searchInput" placeholder="Search..." @input="searchItems">
        <ul>
            <li v-for="item in store.getters.getTeam()" :key="item.id">{{ item.name }}</li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            items: [],
            searchInput: '',
        }
    },
    mounted() {
        this.fetchItems();
    },
    methods: {
        fetchItems() {
            const query = this.searchInput ? `?q=${this.searchInput}` : '';
            axios.get(`http://chessible.pythonanywhere.com/teams${query}`)
                .then(response => {
                    this.items = response.data;
                    this.filteredItems = this.items;
                })
                .catch(error => {
                    console.error(error);
                });
        },
        searchItems() {
            this.fetchItems();
        }
    }
}
</script>
