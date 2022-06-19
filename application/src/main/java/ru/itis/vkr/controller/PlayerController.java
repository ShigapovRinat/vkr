package ru.itis.vkr.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.ModelAndView;
import ru.itis.vkr.dto.SearchPlayersDto;
import ru.itis.vkr.service.PlayerService;

@Controller
@RequiredArgsConstructor
public class PlayerController {

    private final PlayerService playerService;

    @GetMapping("/hockey/search")
    public ModelAndView search() {
        return new ModelAndView("search");
    }

    @PostMapping("/hockey/players")
    public ModelAndView getPlayers(SearchPlayersDto dto) {
        var players = playerService.getPlayersForTeam(dto.getTeam(), dto.getPosition());
        return new ModelAndView("result", "players", players);
    }

}
