-- Performance indexes for Wordle CLI database
-- Improves query performance for common operations

-- Index for user authentication (quick username lookup)
CREATE INDEX idx_users_username ON users(username);

-- Index for finding user's games
CREATE INDEX idx_games_user_id ON games(user_id);

-- Index for finding games by status (active games, completed games)
CREATE INDEX idx_games_status ON games(status);

-- Index for finding guesses by game (showing game history)
CREATE INDEX idx_guesses_game_id ON guesses(game_id);

-- Index for finding guesses by position within a game
CREATE INDEX idx_guesses_game_position ON guesses(game_id, position);

-- Index for completed games (statistics and history)
CREATE INDEX idx_games_completed ON games(completed_at) WHERE completed_at IS NOT NULL;
