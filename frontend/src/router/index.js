import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/signup/landlord',
    name: 'signup-landlord',
    component: () => import('../views/SignupLandlordView.vue')
  },
  {
    path: '/signup/tenant-juridical',
    name: 'signup-tenant-juridical',
    component: () => import('../views/SignupTenantJuridicalView.vue')
  },
  {
    path: '/signup/tenant-natural',
    name: 'signup-tenant-natural',
    component: () => import('../views/SignupTenantNaturalView.vue')
  },
  {
    path: '/signin/admin',
    name: 'signin-admin',
    component: () => import('../views/SigninAdminView.vue')
  },
  {
    path: '/signin/landlord',
    name: 'signin-landlord',
    component: () => import('../views/SigninLandlordView.vue')
  },
  {
    path: '/signin/tenant-juridical',
    name: 'signin-tenant-juridical',
    component: () => import('../views/SigninTenantJuridicalView.vue')
  },
  {
    path: '/signin/tenant-natural',
    name: 'signin-tenant-natural',
    component: () => import('../views/SigninTenantNaturalView.vue')
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('../views/ProfileView.vue')
  },
  {
    path: '/search/map',
    name: 'search-map',
    component: () => import('../views/SearchMapView.vue')
  },
  {
    path: '/search/results',
    name: 'search-results',
    component: () => import('../views/SearchResultsView.vue')
  },
  {
    path: '/places/place',
    name: 'places-place',
    component: () => import('../views/PlacesPlaceView.vue')
  },
  {
    path: '/places/add',
    name: 'places-add',
    component: () => import('../views/PlacesAddView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
