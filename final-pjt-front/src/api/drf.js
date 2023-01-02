const HOST = 'http://localhost:8000/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const COMMENTS = 'comments/'

export default {
    accounts: {
      login: () => HOST + ACCOUNTS + 'login/',
      logout: () => HOST + ACCOUNTS + 'logout/',
      profile: username => HOST + ACCOUNTS + 'profile/' + `${username}/`,
      signup: () => HOST + ACCOUNTS + 'signup/',
      // 유저 로그인 확인
      currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    },
    movies: {
      movie: moviePk => HOST + MOVIES + `${moviePk}/`,
      likemovie: moviePk => HOST + MOVIES + `${moviePk}/` + 'like/',

      likecomment: (moviePk, commentPk) => HOST + MOVIES + `${moviePk}/` + COMMENTS + `${commentPk}/` + 'like/',

      searchmovies: title => HOST + MOVIES + `search/${title}/`,
      question: () => HOST + MOVIES + `question/`, //  설문 제출 post
  
      comments: (moviePk) => HOST + MOVIES + `${moviePk}/` + COMMENTS,
      comment: (moviePk, commentPk) =>  HOST + MOVIES + `${moviePk}/` + COMMENTS + `${commentPk}/`, // 코멘트 삭제
    },
  }