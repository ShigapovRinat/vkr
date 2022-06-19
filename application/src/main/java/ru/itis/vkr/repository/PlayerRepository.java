package ru.itis.vkr.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ru.itis.vkr.model.Player;

import java.util.List;

@Repository
public interface PlayerRepository extends JpaRepository<Player, Long> {

    List<Player> findAllByTeamAndPosition(String team, String position);

    List<Player> findAllByRatingGreaterThanAndTeamNotLikeAndPosition(Double rating, String team, String position);
}
