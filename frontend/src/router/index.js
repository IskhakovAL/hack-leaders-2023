import Vue from 'vue'
import VueRouter from 'vue-router'
import store from "../store"

Vue.use(VueRouter)

const routes = [
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
    component: () => import('../views/SigninTenantNaturalView.vue'),
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('../views/ProfileView.vue'),
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/search/map',
    name: 'search-map',
    component: () => import('../views/SearchMapView.vue'),
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/search/results',
    name: 'search-results',
    component: () => import('../views/SearchResultsView.vue'),
    meta: {
      requiresAuth: true
    }

  },
  {
    path: '/places/place',
    name: 'places-place',
    component: () => import('../views/PlacesPlaceView.vue'),
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/places/add',
    name: 'places-add',
    component: () => import('../views/PlacesAddView.vue'),
    meta: {
      requiresAuth: true
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router


router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    console.log(store.getters.getIsLogin)

    // if (window.$cookies.get('token') === null) {
    if (localStorage.getItem("token") === null) {
      next('/signup/tenant-natural')
    } else {
      next()
    }
  } else {
    if ((to.path.includes("signin") || to.path.includes("signup")) && store.getters.getIsLogin === true) {
      next('/profile')
    } else {
      next()
    }
  }
})
