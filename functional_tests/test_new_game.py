from functional_tests import SeleniumTestCase


class NewGameTest(SeleniumTestCase):
    def setUpTestData(self):
        self.abe = self.create_user(username='abe', password='abepass')
        self.ben = self.create_user(username='ben', password='benpass')
        self.carla = self.create_user(username='carla', password='carlapass')

    def test_users_can_record_a_game(self):
        self.abe_logs_in()
        self.abe_starts_a_new_game_between_ben_and_carla()
        self.records_the_points_for_the_game()
        self.and_is_redirected_to_a_results_page()

    def abe_logs_in(self):
        self.visit('app:login')
        self.fill_out(
            'login-form', {
                'username': 'abe',
                'password': 'abepass'
            },
            submit=True)
        self.assert_current_view('app:user-home')

    def abe_starts_a_new_game_between_ben_and_carla(self):
        self.visit('app:new-game')
        self.assert_current_view('app:new-game')
        self.fill_out(
            'new-game-form', {
                'player_1': self.ben.username,
                'player_2': self.carla.username
            },
            submit=True)

    def records_the_points_for_the_game(self):
        self.assert_current_view('app:score-game')
        self.fill_out(
            'game-form', {
                f'point_{which_point}': self.carla.id
                for which_point in range(1, 11)
            },
            submit=True)

    def and_is_redirected_to_a_results_page(self):
        self.assert_current_view('app:game')
        self.assertElementExists('#status', text='Finished')
        self.assertElementExists('#winner', text=self.carla.username)
        self.assertElementExists('#loser', text=self.ben.username)
        self.assertElementExists('#referee', text=self.abe.username)
        self.assertElementExists('#loser-score', text="0")
        self.assertElementExists('#winner-score', text="10")
