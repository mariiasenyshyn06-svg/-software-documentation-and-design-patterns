class AirbnbService:
    def __init__(self, user_repo, housing_repo, booking_repo, payment_repo):
        self.user_repo = user_repo
        self.housing_repo = housing_repo
        self.booking_repo = booking_repo
        self.payment_repo = payment_repo

    def load_all_data(self, users_csv, housing_csv, bookings_csv, payments_csv):
        self.user_repo.load_from_csv(users_csv)
        self.housing_repo.load_from_csv(housing_csv)
        self.booking_repo.load_from_csv(bookings_csv)
        self.payment_repo.load_from_csv(payments_csv)